from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from bookticket.models import Movie
from bookticket.forms import MovieForm, MovieSearchForm
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required 
def logout_view(request):
	if request.method=="POST":
		logout(request)
		return redirect("/bookticket/")
	else:
		return render(request, "bookticket/confirm_logout.html")
def login_view(request):
	msg=""
	if request.method=="POST":
		username = request.POST.get("username")
		password=request.POST.get("password")
		user = authenticate(username=username,password=password)
		if user:
			login(request, user=user)
			msg = "login successfully"
			redirect_url = request.GET.get("next",None)
			if not redirect_url:
				redirect_url = "/bookticket/index"
			return redirect(redirect_url)
		else:
			msg="failed"
		form = AuthenticationForm(data = request.POST)

	else:
		form = AuthenticationForm()
	return render(request, "bookticket/login.html",
		{"form":form,"message":msg})

@login_required
def delete_movie(request, pk):
	movie = Movie.objects.get(pk=pk)
	msg=""
	if request.method=="POST":
		movie.delete()
		return redirect("/bookticket/movies")
	form = MovieForm(instance=movie)
	return render(request, "bookticket/delete_movie.html",
		{"form":form,"message":msg})

@login_required
def update_movie(request, pk):
	movie = Movie.objects.get(pk=pk)
	msg=""
	if request.method=="POST":
		form = MovieForm(request.POST, request.FILES, instance=movie)
		if form.is_valid():
			form.save()
			return redirect("/bookticket/movies")
		else:
			msg=form._errors
	form = MovieForm(instance=movie)
	return render(request, "bookticket/update_movie.html",
		{"form":form,"message":msg})

@login_required
def create_movie(request):
	msg=""
	if request.method=="POST":

		form = MovieForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return redirect("/bookticket/movies")
		else:
			msg=form._errors

	else:
		form  = MovieForm()
	return render(request,"bookticket/create_movie.html",{"form":form,"message":msg})

def movies_view(request):
	params = request.GET 
	data = Movie.objects.all()

	if params:
		if "twod" in params:
			twod=True if params["twod"]=="on" else False
			data = data.filter(twod=twod)
		if "threed" in params:
			threed=True if params["threed"]=="on" else False
			data = data.filter(threed=threed)
		if "name" in params:
			name=params["name"]
			data = data.filter(name__contains=name)
		if "language" in params:
			language = params["language"]
			if language:
				data = data.filter(languages=language)
		form = MovieSearchForm(data=params)
	else:
		form = MovieSearchForm()
	try:
		num_records_page = settings.NUM_RECORDS_PAGES
	except:
		num_records_page = 100
	pages = Paginator(data, num_records_page)
	
	if "page" in params:
		page_num = params["page"]
		if page_num:
			page_num = int(page_num)
		else:
			page_num =1
	else:
		page_num=1
	data = pages.page(page_num)
	return render(request,"bookticket/movies.html",
		{"data":data,"form":form})
def register_view(request):
	msg=""
	if request.method=="POST":
		# take the data from form
		# insert in to database
		data  = request.POST
		try:
			user = User.objects.create_user(username=data["user_name"],
				password=data["pwd"])
			user.email=data["email_address"]
			user.save()
			msg="User created successfully"
		except Exception as err:
			msg="User name already exist"

	return render(request, "bookticket/register.html",{"message":msg})
def home_view(request):
	return render(request, "bookticket/home.html")

def users_view(request):
	return HttpResponse(["user1","user2","user3","user4"])


'''
def fun(request):
	resp="""
	<table border=1 >
				<tr>
					<th>movie name</th>
					<th>movie cast</th>
					<th>movie description</th>
					<th>movie rating</th>
				</tr>
				<tr>
					<td>jersey</td>
					<td>nani,</td>
					<td>sports,sentiments</td>
					<td>93%</td>
				</tr>
				<tr>
					<td>kalank</td>
					<td>varun</td>
					<td>drama, </td>
					<td>93%</td>
				</tr>
			</table>
	"""
	obj = HttpResponse(resp)
	#print(obj.get())
	return obj
'''