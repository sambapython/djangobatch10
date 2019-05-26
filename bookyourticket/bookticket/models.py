from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError

class ClientRequest(models.Model):
	ip_adress = models.GenericIPAddressField(max_length=250)
	url = models.CharField(max_length=250)
	resp_status = models.CharField(max_length=250,blank=True, null=True)
	is_movie = models.BooleanField(default=False)

class OwnUser(AbstractUser):
	cell = models.IntegerField(blank=True, null=True)

# Create your models here.
def name_validate(value):
	if not value.isalnum():
		raise ValidationError("bnot expecting special symbols in name")
class abs(models.Model):
	""" Its an abstract model. This will not create a table in the database.
        can inherit this model into some other models, then these columns will
        create in thae corresponding tables
	"""
	name = models.CharField(max_length=250, validators=(name_validate,))
	class Meta:
		abstract=True

'''
class UserProfile(OwnUser):
	mobile = models.IntegerField()
class UserProfile1(models.Model):
	user_ptr = models.OneToOneField(OwnUser, on_delete=models.PROTECT)
	mobile = models.IntegerField()
	'''
class Language(models.Model):
	name=models.CharField(max_length=60)

	def __str__(self):
		return self.name

def validate_rating(number):
	if number<1 or number>5:
		raise ValidationError("number should be 1-5")



class Movie(abs):
	#languages=[("t","TELUGU"),("e","ENGLISH"),("h","HINDHI")]
	#name = models.CharField(max_length=300, unique=True)
	description = models.TextField(blank=True, null=True)
	cast = models.CharField(max_length=250,blank=True, null=True)
	languages = models.ManyToManyField(Language)
	twod = models.BooleanField(default=True)
	threed = models.BooleanField(default=False)
	rating = models.IntegerField(default=1, validators=(validate_rating,))
	createdby=models.ForeignKey(OwnUser, blank=True, null=True, on_delete=models.PROTECT)
	poster = models.ImageField(blank=True, null=True)


	def get_data(self):
		data =  {"id":self.id,"name":self.name, "description":self.description,
		"cast":self.cast,"twod":self.twod,"threed":self.threed,
		"rating":self.rating}
		langs = []
		for lang in self.languages.all():
			langs.append(lang.name)
		data.update({"languages":",".join(langs)})
		return data

	def __str__(self):
		return "%s,%s"%(self.name, self.rating)
class Theater(models.Model):
	name=models.CharField(max_length=250)
	address = models.TextField()
	number_seats = models.IntegerField()
	createdby = models.ForeignKey(OwnUser, blank=True, null=True, on_delete=models.PROTECT)
	rating = models.IntegerField(default=1)
	status = models.BooleanField(default=True)
	image = models.ImageField(blank=True, null=True)
	

