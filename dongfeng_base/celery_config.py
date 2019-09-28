from dongfeng_base.consts.queues import TaskQueue

task_routes = {"overwatch.*": {"queue": TaskQueue.OVERWATCH.value}, "scout.*": {"queue": TaskQueue.SCOUT.value}}
accept_content = ["json", "pickle"]
task_serializer = "pickle"
result_serializer = "pickle"
