from django.shortcuts import render

# Create your views here.
def pur_index_view(request):
	return render(request,"pur/index.html")
