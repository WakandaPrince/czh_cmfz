
from django.urls import path, include
from article import views
app_name = 'article'
urlpatterns = [
    path("upload_img/", views.upload_img,name='upload_img'),

]