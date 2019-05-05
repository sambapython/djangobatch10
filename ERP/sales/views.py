from django.shortcuts import render

# Create your views here.
def sales_index_view(request):
	return render(request, "sales/index.html")
