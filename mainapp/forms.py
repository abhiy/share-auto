from django import forms
import datetime
from django.utils.safestring import mark_safe

class phoneForm(forms.Form):
	phoneNumber = forms.IntegerField(label='Enter your phone number:')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class infoForm(forms.Form):
	CHOICES=[('cmps','To Campus'), ('cnb','To CNB')]
	dest = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	date_ = forms.DateField(initial=datetime.date.today, label=mark_safe("<br><br>When do you plan to leave?"), widget=forms.DateInput(format=('%Y-%m-%d')))
	time_ = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label=mark_safe("<br><br>What time?"))

class addMeForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	phoneNumber = forms.CharField(label='Enter your contact number:', max_length=100)

class createListingForm(forms.Form):
	CHOICES=[('cmps','To Campus'), ('cnb','To CNB')]
	dest = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	your_name = forms.CharField(label=mark_safe('<br><br>Your name'), max_length=100)
	phoneNumber = forms.CharField(label=mark_safe('<br><br>Enter your contact number:'), max_length=100)
	date_ = forms.DateField(initial=datetime.date.today, label=mark_safe("<br><br>What date you plan to leave?"), widget=forms.DateInput(format=('%Y-%m-%d')))
	time_ = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label=mark_safe("<br><br>What time?"))