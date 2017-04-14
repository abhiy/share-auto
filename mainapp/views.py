from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import phoneForm 
from .forms import NameForm 

# Create your views here
def startup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = phoneForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            number = form.cleaned_data['phoneNumber']
            context = {'number' : number}
            return render(request, "resp.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = phoneForm()

    return render(request, 'startup.html', {'form': form})

def listings(request, number):
	context = {'number': number}
	return render(request, "resp.html", context)