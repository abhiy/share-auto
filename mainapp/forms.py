from django import forms

class phoneForm(forms.Form):
	phoneNumber = forms.CharField(label='Enter your phone number:', max_length=100)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)