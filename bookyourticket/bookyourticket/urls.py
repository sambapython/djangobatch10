"""bookyourticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', fun),
]
