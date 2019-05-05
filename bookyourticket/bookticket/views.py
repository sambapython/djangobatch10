from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from bookticket.models import Movie
from bookticket.forms import MovieForm
def create_movie(request):
	msg=""
	if request.method=="POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/bookticket/movies")
		else:
			msg=form._errors

	else:
		form  = MovieForm()
	return render(request,"bookticket/create_movie.html",{"form":form,"message":msg})
def movies_view(request):
	all_movies = Movie.objects.all()
	return render(request,"bookticket/movies.html",{"data":all_movies})
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