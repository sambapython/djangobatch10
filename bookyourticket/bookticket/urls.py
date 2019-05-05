from django.urls import path
from bookticket.views import users_view, home_view, register_view,\
movies_view, create_movie
urlpatterns = [
    path('', home_view),
    path('users/', users_view),
    path("register/",register_view),
    path('movies/', movies_view),
    path("create_movie/",create_movie)
    ]