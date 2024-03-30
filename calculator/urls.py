
from django.urls import path

from .views import products_calculator


urlpatterns = [

    path('<v_dish>/<int:v_serv>/', products_calculator, name='calculate'),
    path('<v_dish>/', products_calculator, name='calculate'),
    path('', products_calculator, name='calculate'),
]

