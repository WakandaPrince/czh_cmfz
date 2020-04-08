
from django.urls import path, include
from home import views
urlpatterns = [
    path('index/', views.main, name='home_index'),
    path('login/', views.login, name='login'),
    path('get_code/', views.get_code, name='get_code'),
    path('check_user/', views.check_user, name='check_user'),
]
