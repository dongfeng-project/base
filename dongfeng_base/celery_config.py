from celery.schedules import crontab

# celery beat
CELERYBEAT_SCHEDULE = {
    "get_resource_usage": {"task": "dongfeng_base.tasks.misc.get_resource_usage", "schedule": crontab(minute="*")},
}
