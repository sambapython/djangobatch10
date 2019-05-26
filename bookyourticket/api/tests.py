from django.test import TestCase
from bookticket.models import OwnUser
from rest_framework.test import APIClient

# Create your tests here.
class Movitestcases(TestCase):

	@classmethod
	def tearDownClass(cls):
		cls.client.logout()

	@classmethod
	def setUpClass(cls):
		user = OwnUser.objects.create_user(username="user1",password="user1")
		cls.client = APIClient()
		cls.client.login(username="user1",password="user1")
		

	def test_movie_create(self):
		resp = self.client.post("api/movies/", json={"name":"EFGH",
				"languages":[1,2],
				"twod":True,
				"threed":False,
				"description":"comedy",})
		self.assertTrue(resp.status_code in [200,201], "Movie creation test failed.")
	def test_movie_create1(self):
		print("this is movie creation")
	def test_movie_create2(self):
		print("this is movie creation")

