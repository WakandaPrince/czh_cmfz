
from django.urls import path, include
from slidpic import views
urlpatterns = [
    path("get_all_banner/", views.get_all_banner,name='get_all_banner'),
    path("add_banner/", views.add_banner,name='add_banner'),
    path("edit_banner/", views.edit_banner,name='edit_banner'),
]