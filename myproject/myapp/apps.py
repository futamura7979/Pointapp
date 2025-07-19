from django.apps import AppConfig
from .test import selenium_job
from .daypoint import run_selenium_script,login

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    selenium_job(run_selenium_script)
    
