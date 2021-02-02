from django.urls import path, include
from . import views

app_name = 'lnkzio'

urlpatterns = [
    path('', views.index,  name='index'),
    path('<int:code>', views.forward, name='forward'),
    path('shorturl/', views.shorturl, name='shorturl')
]