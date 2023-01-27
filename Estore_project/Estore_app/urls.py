from django.contrib import admin
from django.urls import path, include
from .views import index, signup, Login

urlpatterns = [
    path('', index, name='homepage'),
    path('signup',signup.as_view()),
    path('login', Login.as_view())
]