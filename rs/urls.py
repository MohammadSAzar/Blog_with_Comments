from django.urls import path
from .views import load_cities, load_districts, real_estate_create

urlpatterns = [
    path('', real_estate_create, name='real_estate_create'),
    path('load_cities/', load_cities, name='load_cities'),
    path('load_districts/', load_districts, name='load_districts'),
]

