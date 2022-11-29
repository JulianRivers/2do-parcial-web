from django.urls import path
from . import views

app_name='aspirante'
urlpatterns = [
    path('', views.index, name='index'),
    path('aspirante/', views.aspirante, name='aspirante'),
    path('registrar/', views.registrar, name='registrar'),
]