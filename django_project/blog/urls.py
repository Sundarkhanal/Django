from django.urls import path
from . import views         #. refer to current module

urlpatterns = [
    path('', views.home, name='blog-home'),    #'' this is for home page
]
