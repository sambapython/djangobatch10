from django.urls import path, re_path
from bookticket.views import users_view, home_view, register_view,\
movies_view, create_movie, update_movie, delete_movie
urlpatterns = [
    path('', home_view),
    path('users/', users_view),
    path("register/",register_view),
    path('movies/', movies_view),
    path("create_movie/",create_movie),
    re_path("update_movie/(?P<pk>[0-9]+)", update_movie),# update_movie(req_obj, pk=10)
    re_path("delete_movie/(?P<pk>[0-9]+)", delete_movie),
    ]