from django.apps import AppConfig


class BookticketConfig(AppConfig):
    name = 'bookticket'

    def ready(self):
    	import bookticket.signals
