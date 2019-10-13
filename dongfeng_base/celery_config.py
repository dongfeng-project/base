from dongfeng_base.consts.queues import TaskQueue

task_routes = {
    "base.*": {"queue": TaskQueue.BASE.value},
    "overwatch.*": {"queue": TaskQueue.OVERWATCH.value},
    "scout.*": {"queue": TaskQueue.SCOUT.value},
}
accept_content = ["json", "pickle"]
task_serializer = "pickle"
result_serializer = "pickle"
