from django.apps import AppConfig
from .test import start
from .daypoint import run_selenium_script,login

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    # def ready(self):
    #     start(run_selenium_script)
    
