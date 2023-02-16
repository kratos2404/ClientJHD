from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('maps/', views.maps, name='maps'),
    path('about/', views.about, name='about'),
    path('design/', views.design, name='design'),
    path('contact/', views.contact, name='contact'),
    #path('address/', views.address, name='address'),
]