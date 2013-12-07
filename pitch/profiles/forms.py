from django.forms import ModelForm
from profiles.models import ProfileDetail

class ProfileDetailForm(ModelForm):
	class Meta:
		model = ProfileDetail
		fields = ['dob', 'state_of_residency', 'city_of_residency', 'state_of_office', 'city_of_office']
