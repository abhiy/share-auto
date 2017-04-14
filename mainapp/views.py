from django.shortcuts import render

# Create your views here.
def startup(request):
	return render(request, "startup.html")

def listings(request, number):
	context = {'number': number}
	return render(request, "resp.html", context)