from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
	name=models.CharField(max_length=60)


class Movie(models.Model):
	#languages=[("t","TELUGU"),("e","ENGLISH"),("h","HINDHI")]
	name = models.CharField(max_length=300)
	description = models.TextField(blank=True, null=True)
	cast = models.CharField(max_length=250,blank=True, null=True)
	languages = models.ManyToManyField(Language)
	twod = models.BooleanField(default=True)
	threed = models.BooleanField(default=False)
	rating = models.IntegerField(default=1)
	createdby=models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)

	

