from django.forms import ModelForm, Form
from bookticket.models import Movie, Language
from django import forms

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__" #["name","description","twod"]

class MovieSearchForm(Form):
    languages=[(row.id,row.name) for row in Language.objects.all()]
    languages.insert(0,('',''))
    name= forms.CharField(max_length=250, required=False)
    language = forms.ChoiceField(required=False, choices=languages)
    twod = forms.CharField(widget=forms.widgets.CheckboxInput, required=False)
    threed = forms.CharField(widget=forms.widgets.CheckboxInput, required=False)
    page = forms.CharField(max_length=10, required=False)
    