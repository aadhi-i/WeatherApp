from django.urls import path
from . import views

urlpatterms =[
    path('',views.home, name='home'),
]