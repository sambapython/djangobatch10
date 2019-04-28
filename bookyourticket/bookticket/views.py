from django.shortcuts import render
from django.http import HttpResponse
def register_view(request):
	if request.method=="POST":
		# take the data from form
		# insert in to database
		print(request.POST)
	return render(request, "register.html")
def home_view(request):
	return render(request, "home.html")

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