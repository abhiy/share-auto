from django import forms

class phoneForm(forms.Form):
	phoneNumber = forms.CharField(label='Enter your phone number:')