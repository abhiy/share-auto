from django import forms
import datetime
class phoneForm(forms.Form):
	phoneNumber = forms.IntegerField(label='Enter your phone number:')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class infoForm(forms.Form):
	CHOICES=[('cmps','To Campus'), ('cnb','To CNB')]
	dest = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	date_ = forms.DateField(initial=datetime.date.today, label="When do you plan to leave?", widget=forms.DateInput(format=('%Y-%m-%d')))
	time_ = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="What time?")

class addMeForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	phoneNumber = forms.CharField(label='Enter your contact number:', max_length=100)
	numberlisting = forms.CharField(widget=forms.HiddenInput())
	header = forms.CharField(widget=forms.HiddenInput())

class createListingForm(forms.Form):
	CHOICES=[('cmps','To Campus'), ('cnb','To CNB')]
	dest = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	your_name = forms.CharField(label='Your name', max_length=100)
	phoneNumber = forms.CharField(label='Enter your contact number:', max_length=100)
	date_ = forms.DateField(initial=datetime.date.today, label="When date you plan to leave?", widget=forms.DateInput(format=('%Y-%m-%d')))
	time_ = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="What time?")