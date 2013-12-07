from django.db import models

from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

'''
Each registered user has to fill out a detailed profile.
'''

class ProfileDetail(models.Model):
	user = models.OneToOneField(User,unique=True, verbose_name=('user'), related_name='profile_details')
	dob = models.DateField(blank = True, null = True)
	state_of_residency = models.CharField(verbose_name='State of Residency: ', max_length = 25, blank = True, null = True)
	city_of_residency = models.CharField(verbose_name='City of Residency: ',max_length = 25, blank = True, null = True)
	state_of_office = models.CharField(verbose_name='State of Office: ',max_length = 25, blank = True, null = True)
	city_of_office = models.CharField(verbose_name='City of Residency: ',max_length = 25, blank = True, null = True)
	
	def __unicode__(self, ):
		return self.user.username