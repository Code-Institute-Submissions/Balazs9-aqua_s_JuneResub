from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('mineral/', views.mineral_water, name='mineral_water'),
    path('sport_drink/', views.sport_drink, name='sport_drink'),
    path('machine/', views.water_dispenser, name='water_dispenser'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]