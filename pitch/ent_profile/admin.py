from django.contrib import admin
from django.db import models
from .models import Venture
'''
class EntrepreneurProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = EntProfile

admin.site.register(EntProfile, EntrepreneurProfileAdmin)
'''

class VentureAdmin(admin.ModelAdmin):
	class Meta:
		model = Venture

admin.site.register(Venture, VentureAdmin)