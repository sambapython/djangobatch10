from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bookticket.models import Movie,Language
from rest_framework import status

class MovieAPIView(APIView):
	def post(self,request, format=None):
		
		data = request.data
		languages = data.pop("languages")
		movie = Movie(**data)
		try:
			movie.save()
			for lang in languages:
				movie.languages.add(Language.objects.get(id=lang))
			return Response("movie created successfully!!",
				status = status.HTTP_201_CREATED)
		except Exception as err:
			return Response("movie not created: issue:%s"%err,
				status=status.HTTP_400_BAD_REQUEST)
	def put(self, request, pk, format=None):
		pass
	def get(self, request, pk=None, format=None):
		movies = Movie.objects.all()
		res= [] 
		for movie in  movies:
			res.append(movie.get_data())
		return Response(res)
	def delete(self, request, pk, format=None):
		movie = Movie.objects.get(id=pk)
		movie.delete()
		return Response("Movie: %s deleted successdfully "%movie.name)