from django import forms
from mentor.models import  Profile
'''
class EntProfileForm(forms.ModelForm):

	class Meta:
		model = EntProfile
		fields = ('name', 'dob', 'state_of_residency', 'city_of_residency', 'state_of_office', 'city_of_office')
'''

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'address', 'zipcode']
		

