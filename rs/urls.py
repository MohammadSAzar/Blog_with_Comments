from django.urls import path
from . import views

urlpatterns = [
    path('', views.real_estate_create, name='real_estate_create'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
]
