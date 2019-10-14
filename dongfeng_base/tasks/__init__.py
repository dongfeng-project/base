from pathlib import Path

from celery import Celery, platforms
from celery.worker.control import inspect_command
from dongfeng_base.consts.tasks import TaskName
from dongfeng_base.utils.worker import get_resource_usage

from .example import example_task


def auto_register(entry: str, app: Celery):
    """
    自定义的任务自动发现
    :param entry: 入口文件
    :param app: Celery示例
    :return:
    """
    path = Path(entry)
    if path.is_file():
        base_dir = path.parent
    elif path.is_dir():
        base_dir = path
    else:
        return

    p = base_dir.glob("*.py")
    relative_names = (x.name.replace(".py", "") for x in p if x.is_file() and "__init__" not in x.name)

    for name in relative_names:
        app.autodiscover_tasks(packages=(base_dir.name,), related_name=name, force=True)

    app.autodiscover_tasks(packages=("dongfeng_base.tasks",))


def debug_worker(env: str):
    if env == "dev":
        platforms.C_FORCE_ROOT = True


@inspect_command(name=TaskName.OverWatch.RESOURCE_USAGE.value)
def resource_usage(state):
    result = get_resource_usage()
    return result.__dict__


# 拆分的任务需要在这里手动注册，这样才能在其他包里使用app.autodiscover_tasks查找任务
tasks = (example_task,)
