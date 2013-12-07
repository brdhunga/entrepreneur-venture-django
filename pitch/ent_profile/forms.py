from django import forms
from .models import  Venture
'''
class EntProfileForm(forms.ModelForm):

	class Meta:
		model = EntProfile
		fields = ('name', 'dob', 'state_of_residency', 'city_of_residency', 'state_of_office', 'city_of_office')
'''

class VentureForm(forms.ModelForm):

	class Meta:
		model = Venture		