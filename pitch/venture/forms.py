from django.forms import ModelForm
from venture.models import Venture

class VentureForm(ModelForm):
	class Meta:
		model = Venture
		exclude = ['user']
		
