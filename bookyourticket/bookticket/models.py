from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Language(models.Model):
	name=models.CharField(max_length=60)

	def __str__(self):
		return self.name

def validate_rating(number):
	if number<1 or number>5:
		raise ValidationError("number should be 1-5")



class Movie(models.Model):
	#languages=[("t","TELUGU"),("e","ENGLISH"),("h","HINDHI")]
	name = models.CharField(max_length=300, unique=True)
	description = models.TextField(blank=True, null=True)
	cast = models.CharField(max_length=250,blank=True, null=True)
	languages = models.ManyToManyField(Language)
	twod = models.BooleanField(default=True)
	threed = models.BooleanField(default=False)
	rating = models.IntegerField(default=1, validators=(validate_rating,))
	createdby=models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)

	def __str__(self):
		return "%s,%s"%(self.name, self.rating)

	

