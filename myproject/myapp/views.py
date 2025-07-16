from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .App import run_selenium_script
from .tests import test_selenium_script


def pointget(request):
    run_selenium_script
    return HttpResponse("Seleniumスクリプトを実行しました。")

def index(request):
    return render(request, 'myapp/sample.html')

