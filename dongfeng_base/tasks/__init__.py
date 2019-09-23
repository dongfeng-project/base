from .misc import *

# 拆分的任务需要在这里手动注册，这样才能在其他包里使用app.autodiscover_tasks查找任务
tasks = (get_ip, get_resource_usage)
