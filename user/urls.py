from django.urls import path
from user import views
app_name = 'user'
urlpatterns = [
    path("get_all_user/", views.get_all_user,name='get_all_user'),
    path("add_user/", views.add_user,name='edit_user'),
    path("edit_user/", views.edit_user,name='edit_user'),
    path("render_added_echart/", views.render_added_echart,name='render_added_echart'),
    path("render_num_map/", views.render_num_map,name='render_num_map'),
    path("get_added_num/", views.get_added_num,name='get_added_num'),
    path("get_map_data/", views.get_map_data,name='get_map_data'),
]