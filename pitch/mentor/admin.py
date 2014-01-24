from django.contrib import admin
from django.db import models
from .models import Profile, Mentor_Venture





class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile
		prepopulated_fields = {'slug':('name',),}

admin.site.register(Profile, ProfileAdmin)






class Mentor_VentureAdmin(admin.ModelAdmin):
	class Meta:
		model = Mentor_Venture

admin.site.register(Mentor_Venture, Mentor_VentureAdmin)



