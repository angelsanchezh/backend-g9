
from django.urls import path
from .views import saludar,parametros,PruebaApiView



urlpatterns = [

    path('inicio/',saludar),
    path('parametros/<nombre>',parametros),
    path ('prueba', PruebaApiView.as_view()),
]

