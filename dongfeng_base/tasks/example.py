from celery import shared_task

from ..consts.tasks import TaskName
from ..utils.worker import get_resource_usage


@shared_task(name=TaskName.Base.EXAMPLE.value)
def example_task():
    return get_resource_usage()
