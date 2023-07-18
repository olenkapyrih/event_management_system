from django.urls import path
from app import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.health_check, name='health_check')
]