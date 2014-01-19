import datetime
from django.db import models
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
	def get_by_natural_key(self, username, name, address, zipcode):
		return self.get(username = username, name = name, address = address, zipcode = zipcode)


class Profile(models.Model):
	objects = ProfileManager()

	username = models.OneToOneField(User)
	name = models.CharField(max_length = 100, blank = True, null = True)
	address = models.CharField(max_length = 200, blank = True, null = True)
	zipcode = models.IntegerField(max_length = 6, blank = True, null = True )

	def natural_key(self):
		return[self.username]

	def __unicode__(self, ):
		if self.name is None:
			return str(self.username)
		else:
			return str(self.name)
		

class Mentor_Venture(models.Model):
	# Page 1
	applicant = models.CharField(max_length = 200, blank = True, null = True)
	name = models.CharField(max_length = 200, blank = True, null = True)
	nickname = models.CharField(max_length = 200,  blank = True, null = True)
	industry = models.CharField(max_length = 200,  blank = True, null = True)
	website = models.CharField(max_length = 50,  blank = True, null = True)
	legally_formed = models.BooleanField(default = True)
	other_team_members = models.CharField(max_length = 200,  blank = True, null = True)
	project_leader = models.BooleanField(default = True)
	#Another Page
	chracterstics = models.TextField()
	skills_lacking = models.TextField()
	# Page 2
	target_customers = models.TextField()
	needs_satisfied = models.TextField()
	competitors = models.TextField()
	free_alternatives = models.TextField()
	# Page 3
	how_meets_customer_needs = models.TextField()
	how_differentiate = models.TextField()
	describe_mvp = models.TextField() #mvp = minimal viable product
	#Page 4
	launch_date = models.DateField(auto_now = False, auto_now_add = False)
	investment_needed = models.TextField()
	willing_to_relocate = models.BooleanField(default = False)
	creation_date = models.DateField(auto_now = False, auto_now_add = False)
	remarks = models.TextField(null = True, blank = True)


	def __unicode__(self, ):
		return self.name


		#generate random key
		#http://stackoverflow.com/questions/3928016/django-auto-generating-unique-model-fields-and-recursively-calling-auto-generat


class Clients(models.Model):
	client_username = models.CharField(max_length = 50, null = True, blank = True)

	def __unicode__(self, ):
		return self.client_username
