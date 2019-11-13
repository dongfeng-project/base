import os
import platform
import subprocess
import time
from threading import Timer

import psutil


class Command(object):
    is_linux = platform.system() == "Linux"

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.process = None

    def __kill(self):
        """
        终止进程
        :return:
        """
        try:
            pid = self.process.pid
            root_proc = psutil.Process(pid)
            procs = root_proc.children(recursive=True)
            for p in procs:
                p.send_signal(sig=psutil.signal.SIGKILL)
        except (ProcessLookupError, psutil.NoSuchProcess):
            pass

    def __timeout_callback(self):
        """
        超时回调
        :return:
        """
        return self.__kill()

    def block_run(self, cmd: str) -> bytes:
        """
        阻塞式运行
        :param cmd:
        :return:
        """
        self.process = subprocess.Popen(
            args=cmd,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            shell=True,
            preexec_fn=os.setsid if self.is_linux else None,
        )

        start_time = time.time()

        if self.timeout == 0:
            return self.process.stdout.read()

        while True:
            if self.process.poll() is not None:
                break
            time_used = time.time() - start_time
            if self.timeout and time_used > self.timeout:
                self.__kill()
                break
            time.sleep(0.1)

        return self.process.stdout.read()

    def async_run(self, cmd: str):
        """
        异步运行
        :param cmd:
        :return:
        """
        self.process = subprocess.Popen(
            args=cmd,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            shell=True,
            preexec_fn=os.setsid if self.is_linux else None,
        )
        timer = Timer(self.timeout, self.__timeout_callback)
        timer.start()

        try:
            for stdout_line in iter(self.process.stdout.readline, b""):
                if self.process.poll() is not None:
                    # 进程结束
                    raise StopIteration
                else:
                    yield stdout_line
        except StopIteration:
            # 先杀死进程再停止迭代
            self.__kill()
            raise
        finally:
            timer.cancel()
            self.process.stdout.close()
            self.__kill()

    def run(self, cmd: str, is_async: bool = False):
        """
        命令执行入口
        :param cmd:命令
        :param is_async:是否异步执行
        :return:
        """
        if is_async:
            return self.async_run(cmd=cmd)
        else:
            return self.block_run(cmd=cmd)
