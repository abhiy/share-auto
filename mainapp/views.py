from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime, date, time
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
            #return render(request, "resp.html", context)

            db_cnb = ToCNB.objects.filter(phoneNumber = number)
            db_cmps = ToCampus.objects.filter(phoneNumber = number)
            context = {'obj_cnb': db_cnb, 'obj_cmps': db_cmps}
            return render(request, "myListings.html", context)

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
            date = infoForm_.cleaned_data['date_']
            time = infoForm_.cleaned_data['time_']
            dest = infoForm_.cleaned_data['dest']
            datetime_ = datetime.datetime.combine(date, time)

            ### Maintaining the Database ###
            # now = datetime.now()
            # elapsed = now - date
            # ToCNB.objects.filter(elapsed__range = (1, 10000))

            time_start = datetime_ - datetime.timedelta(hours = 1)
            time_end = datetime_ + datetime.timedelta(hours = 1)
            if(dest == 'cnb'):
                db = ToCNB.objects.filter(datetime__range=(time_start, time_end))
                addMeForm_ = addMeForm()
                context = {'obj' : db, 'header' : "ToCNB", 'form' : addMeForm_}

            elif (dest == 'cmps'):
                db = ToCampus.objects.filter(datetime__range=(time_start, time_end))
                addMeForm_ = addMeForm()
                context = {'obj' : db, 'header' : "ToCampus", 'form' : addMeForm_}


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
            name = addMeForm_.cleaned_data['your_name']
            userphone = addMeForm_.cleaned_data['phoneNumber']
            phonenumber = request.POST.get("numberlisting", None)
            db = request.POST.get("header", None)


            if db == "ToCNB":
                entry = ToCNB.objects.get(phoneNumber=phonenumber)
                entry.occupancy = entry.occupancy + 1
                entry.save()
            elif db == 'ToCampus':
                entry = ToCampus.objects.get(phoneNumber=phonenumber)
                entry.occupancy = entry.occupancy + 1
                entry.save()
                

            user = Users(phoneNumberListing = phonenumber, userPhone = userphone, userName = name)
            user.save()
            return render(request, 'successfullyAdded.html')

        else:
            addMeForm_ = addMeForm()
            context = {'form' : addMeForm_ }
            return render(request, 'startup.html', context)

    # if a GET (or any other method) we'll create a blank form

    context = {'infoForm' : infoForm_, 'phoneForm' : phoneForm_ }
    return render(request, 'startup.html', context)

def goToCreateListing(request):
    createListingForm_ = createListingForm()
    return render(request, 'goToCreateListing.html', {'form': createListingForm_})

def createListing(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        createListingForm_ = createListingForm(request.POST)
        if createListingForm_.is_valid():
            dest = createListingForm_.cleaned_data['dest']
            date = createListingForm_.cleaned_data['date_']
            time = createListingForm_.cleaned_data['time_']
            datetime_ = datetime.datetime.combine(date, time)
            dest = createListingForm_.cleaned_data['dest']
            name = createListingForm_.cleaned_data['your_name']
            userphone = createListingForm_.cleaned_data['phoneNumber']
            datetime_ = datetime.datetime.combine(date, time)
            occupancy = 1
            context = {'form': createListingForm_}

            if (dest == 'cnb'):
                entry = ToCNB(datetime = datetime_, name = name, occupancy=occupancy, phoneNumber=userphone)
                entry.save()
            elif (dest == 'cmps'):
                entry = ToCampus(datetime=datetime_, name = name, occupancy=1, phoneNumber=userphone)
                entry.save()

    else:
        createListingForm_ = createListingForm()
    return render(request, 'successfullyAdded.html')