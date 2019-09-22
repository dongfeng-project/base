from celery.schedules import crontab

# celery beat
CELERYBEAT_SCHEDULE = {"get_resource_usage": {"task": "tasks.get_resource_usage", "schedule": crontab(second="*/10")}}
