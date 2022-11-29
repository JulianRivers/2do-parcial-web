from django.urls import path
from . import views

app_name='aspirante'
urlpatterns = [
    path('', views.index, name='index')
]