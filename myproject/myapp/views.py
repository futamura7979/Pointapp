from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .daypoint import run_selenium_script
from .readpoint import readpoint_get


def pointget(request):
    run_selenium_script()
    return HttpResponse("Seleniumスクリプトを実行しました。")

def pointget2(request):
    readpoint_get()
    return HttpResponse("Seleniumスクリプトを実行しました。")

def index(request):
    return render(request, 'myapp/sample.html')

