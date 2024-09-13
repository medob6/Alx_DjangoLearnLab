from django.urls import path
from . import views

# here i should creat my urls

urlpatterns = [
    path('home/', views.home , name = 'home')
]