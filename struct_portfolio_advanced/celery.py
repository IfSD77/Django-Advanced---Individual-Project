import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'struct_portfolio_advanced.settings')

app = Celery('struct_portfolio_advanced')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
