
from django.urls import path, include
from main import views
urlpatterns = [
    path('main/', views.main, name='main'),
]
