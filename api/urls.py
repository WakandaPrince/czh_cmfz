
from django.urls import path, include
from api import views
app_name = 'api'
urlpatterns = [
    path("first_page/", views.first_page,name='first_page'),

]