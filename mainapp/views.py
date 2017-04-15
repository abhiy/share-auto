from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime
from .forms import * 
from .models import *

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
            date = infoForm_.cleaned_data['date_']
            time = infoForm_.cleaned_data['time_']
            dest = infoForm_.cleaned_data['dest']
            datetime_ = datetime.datetime.combine(date, time)
            time_start = datetime_ - datetime.timedelta(hours = 1)
            time_end = datetime_ + datetime.timedelta(hours = 1)
            if(dest == 'cnb'):
            	db = ToCNB.objects.filter(datetime__range=(time_start, time_end))
            # context = {'number' : number}
            context = {'obj' : db}
            return render(request, "toCNB.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        phoneForm_ = phoneForm()
        infoForm_ = infoForm()
    context = {'infoForm' : infoForm_, 'phoneForm' : phoneForm_ }
    return render(request, 'startup.html', context)	

def addToListing(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
    	addMeForm_ = addMeForm(request.POST)
    	if addMeForm_.is_valid():
    		phonenumber = addForm_.cleaned_data['numberlisting']
    		name = addForm_.cleaned_data['your_name']
    		userphone = addForm_.cleaned_data['phoneNumber']
    		db = addMeForm(phoneNumberListing = phonenumber,  userPhone = userphone, userName = name)
        	

    # if a GET (or any other method) we'll create a blank form
    else:
        phoneForm_ = phoneForm()
        infoForm_ = infoForm()
    context = {'infoForm' : infoForm_, 'phoneForm' : phoneForm_ }
    return render(request, 'startup.html', context)	

# def createListing(request):
# 	# if this is a POST request we need to process the form data
#     if request.method == 'POST':
#     	createListingForm_ = createListingForm(request.POST)
#     	if createListingForm_.is_valid():
#     		date = infoForm_.cleaned_data['date_']
# 			time = infoForm_.cleaned_data['time_']
# 			dest = infoForm_.cleaned_data['dest']
#     		name = createListingForm_.cleaned_data['name']
#     		userphone = createListingForm_.cleaned_data['userphone']
#     		datetime_ = datetime.datetime.combine(date, time)

    		


#     else:
#         phoneForm_ = phoneForm()
#         infoForm_ = infoForm()
#     context = {'infoForm' : infoForm_, 'phoneForm' : phoneForm_ }
#     return render(request, 'startup.html', context)	


