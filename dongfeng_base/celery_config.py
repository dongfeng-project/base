from dongfeng_base.consts.queues import TaskQueue

task_routes = {"overwatch.*": {"queue": TaskQueue.OVERWATCH.value}, "scout.*": {"queue": TaskQueue.SCOUT.value}}
