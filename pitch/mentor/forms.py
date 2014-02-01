from django import forms
from mentor.models import  Profile, Mentor_Venture
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
		

class Mentor_VentureForm(forms.ModelForm):
	class Meta:
		model = Mentor_Venture
		exclude = ['user', 'unique_id']

