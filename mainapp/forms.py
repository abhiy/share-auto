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