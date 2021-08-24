# -*- coding: utf-8 -*-

# celery multi start celery_tasks -A celery_task -l info --autoscale=50,5 #celery并发数，最多50个，最少5个
# celery -A celery_tasks beat -l info
from __future__ import absolute_import, unicode_literals
from celery import Celery, platforms
import os
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops_backend.settings")
app = Celery('mycelery', broker=settings.BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)
app.conf.timezone = 'Asia/Shanghai'
app.config_from_object("django.conf:settings")
app.conf.update(
    result_expires=3600,
)
app.conf.beat_schedule = {
    'autosc': {
        'task': 'images.tasks.auto_sc',
        'schedule': crontab(hour=13, minute=19)
    }
}

# 自动从所有已注册的django app中加载任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
platforms.C_FORCE_ROOT = True

