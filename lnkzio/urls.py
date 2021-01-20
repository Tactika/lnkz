from django.urls import path, include
from . import views

app_name = 'lnkzio'

urlpatterns = [
    path('', views.index,  name='index'),
]