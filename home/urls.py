
from django.urls import path, include
from home import views
urlpatterns = [
    path('index/', views.main, name='home_index'),
    path('login/', views.login, name='login'),
]
