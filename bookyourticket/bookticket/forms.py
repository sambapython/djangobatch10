from django.forms import ModelForm
from bookticket.models import Movie

class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = "__all__" #["name","description","twod"]
class MovieSearchForm(MovieForm):
	class Meta:
		model=Movie
		fields = ["name","rating","twod","threed"]


		