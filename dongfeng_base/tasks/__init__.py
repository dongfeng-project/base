from celery.worker.control import inspect_command

from dongfeng_base.consts.tasks import TaskName
from dongfeng_base.utils.worker import get_resource_usage


@inspect_command(name=TaskName.OverWatch.RESOURCE_USAGE.value)
def resource_usage(state):
    result = get_resource_usage()
    return result.__dict__


# 拆分的任务需要在这里手动注册，这样才能在其他包里使用app.autodiscover_tasks查找任务
tasks = ()
