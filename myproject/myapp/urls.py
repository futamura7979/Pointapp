from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('pointget', views.pointget, name='pointget'),
    path('pointget2', views.pointget2, name='pointget2')
]