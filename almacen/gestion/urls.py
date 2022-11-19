
from django.urls import path
from .views import saludar,parametros,PruebaApiView,DepartamentosApiView,DepartamentoApiview



urlpatterns = [

    path('inicio/',saludar),
    path('parametros/<nombre>',parametros),
    path ('prueba', PruebaApiView.as_view()),
    path('departamentos/',DepartamentosApiView.as_view()),
    path('departamento/<int:pk>',DepartamentoApiview.as_view())
]

