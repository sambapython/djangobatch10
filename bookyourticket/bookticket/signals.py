from django.db.models.signals import pre_save, post_save
from bookticket.models import ClientRequest
from django.dispatch import receiver 
from bookticket.models import Movie

@receiver(post_save, sender = Movie)
def update_request(sender, instance, **kwargs):
	lcr = ClientRequest.objects.last()
	lcr.is_movie=True
	lcr.save()