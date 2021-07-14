# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import Celery, platforms
import os
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops_backend.settings")
app = Celery('mycelery')
app.conf.timezone = 'Asia/Shanghai'
app.config_from_object("django.conf:settings")
app.conf.beat_schedule = {
    'autosc': {
        'task': 'images.tasks.auto_sc',
        'schedule': crontab(hour=13, minute=19)
    }
}
app.autodiscover_tasks()
platforms.C_FORCE_ROOT = True