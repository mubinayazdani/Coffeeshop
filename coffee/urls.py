from django.urls import path
from .views import *



urlpatterns = [

    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('team/',team, name='team'),
    path('service/',service, name='service'),
    path('connect/',connect, name='connect')
]