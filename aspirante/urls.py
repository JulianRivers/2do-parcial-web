from django.urls import path
from . import views

app_name='aspirante'
urlpatterns = [
    path('', views.index, name='index'),
    path('aspirante/', views.listar, name='aspirante'),
    path('registrar/', views.registrar_aspirante, name='registrar'),
    path('aspirantes/<int:cargo>', views.listar_cargo, name='cargo')
]