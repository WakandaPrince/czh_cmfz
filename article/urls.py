
from django.urls import path, include
from article import views
app_name = 'article'
urlpatterns = [
    path("upload_img/", views.upload_img,name='upload_img'),
    path("get_all_img/", views.get_all_img,name='get_all_img'),
    path("add_article/", views.add_article,name='add_article'),
    path("get_all_article/", views.get_all_article,name='get_all_article'),
    path("edit_article/", views.edit_article,name='edit_article'),
]