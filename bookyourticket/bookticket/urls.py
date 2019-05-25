from django.urls import path, re_path
from bookticket.models import Theater
from bookticket.views import users_view, home_view, register_view,\
movies_view, create_movie, update_movie, delete_movie, login_view,\
logout_view
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView,\
    ListView
from django.contrib.auth.views import login_required 
urlpatterns = [
    #path('', home_view),
    path("logout",logout_view),
    path("index/",login_required(TemplateView.as_view(template_name="bookticket/index.html"))),
    path('',TemplateView.as_view(template_name="bookticket/home.html")),
    path('users/', users_view),
    path("register/",register_view),
    re_path('movies/(?P<pk>[0-9]+)', movies_view),
    path('movies/', movies_view),
    path("create_movie/",create_movie),
    re_path("update_movie/(?P<pk>[0-9]+)", update_movie),# update_movie(req_obj, pk=10)
    re_path("delete_movie/(?P<pk>[0-9]+)", delete_movie),
    path("create_theater/",login_required(CreateView.as_view(
    		model = Theater,
    		fields="__all__",
    		#template_name="booketicket/theater_form.html"
    		success_url = "/bookticket/theaters/",
    	))),
    re_path("update_theater/(?P<pk>[0-9]+)",login_required(UpdateView.as_view(
    		model = Theater,
    		fields="__all__",
    		#template_name="booketicket/theater_form.html"
    		success_url = "/bookticket/theaters/",
    	))),
   
    re_path("delete_theater/(?P<pk>[0-9]+)",login_required(UpdateView.as_view(
    		model = Theater,
    		fields=["status"],
    		#template_name="booketicket/theater_form.html"
    		success_url = "/bookticket/theaters/",
    	))),
    path("theaters/", ListView.as_view(
    		model = Theater,
    		#fields = ["name","address","number_seats","rating"]
    	)),
    path("login/",login_view)

    ]
'''
    re_path("delete_theater/(?P<pk>[0-9]+)",DeleteView.as_view(
    		model = Theater,
    		#template_name="bookticket/theater_confirm_delete.html",
    		success_url = "/booketicket/theaters/",
    	)),
'''