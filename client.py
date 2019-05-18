import requests
url = "http://localhost:8000/api/movies"
resp = requests.get(url)
print(resp)
print(resp.json())
'''
resp = requests.get("http://localhost:8000/api/movies/3")

resp = requests.post("http://localhost:8000/api/movies", 
	json={"name":"ABCD","twod":True,"threed":False,
	"description":"It's a comdey movie"})


resp = requests.put("http://localhost:8000/api/movies/3")

resp = requests.delete("http://localhost:8000/api/movies/4")

'''

print(resp.json())