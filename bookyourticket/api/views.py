from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Reponse

# Create your views here.
class MovieAPIView(APIView):
	def post(self,request, format=None):
		pass
	def put(self, request, pk, format=None):
		pass
	def get(self, request, pk=None, format=None):
		return Reponse(["movie1","movie2"])
	def delete(self, request, pk, format=None):
		pass