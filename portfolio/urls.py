from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    
    path('contact/', views.contact, name = 'contact'),
    path('servicess/', views.servicess, name = 'servicess'),
    
   
]