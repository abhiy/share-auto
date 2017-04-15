from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import * 

# Create your views here
def startup(request):
    phoneForm_ = phoneForm()
    infoForm_ = infoForm()
    context = {'infoForm' : infoForm_, 'phoneForm' : phoneForm_ }
    return render(request, 'startup.html', context)

def myListings(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        phoneForm_ = phoneForm(request.POST)
        # check whether it's valid:
        if phoneForm_.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            number = phoneForm_.cleaned_data['phoneNumber']
            context = {'number' : number}
            return render(request, "resp.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        phoneForm_ = phoneForm()
        infoForm_ = infoForm()
    context = {'infoForm' : infoForm_, 'phoneForm' : phoneForm_ }
    return render(request, 'startup.html', context)	

def showListings(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        infoForm_ = infoForm(request.POST)
        # check whether it's valid:
        if infoForm_.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            number = infoForm_.cleaned_data['phoneNumber']
            context = {'number' : number}
            return render(request, "resp.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        phoneForm_ = phoneForm()
        infoForm_ = infoForm()
    context = {'infoForm' : infoForm_, 'phoneForm' : phoneForm_ }
    return render(request, 'startup.html', context)	
