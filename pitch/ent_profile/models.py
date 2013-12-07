import datetime
from django.db import models
from usertype.models import MyUser as User
'''
class EntProfile(models.Model):

	user = models.OneToOneField(User, unique = True)
	name = models.CharField(max_length = 50, blank = True, null = True)
	dob = models.DateTimeField(blank = False, null = True)
	state_of_residency = models.CharField(max_length = 15, blank = True, null = True)
	city_of_residency = models.CharField(max_length = 20, blank = True, null = True)
	state_of_office = models.CharField(max_length = 15, blank = True, null = True)
	city_of_office = models.CharField(max_length = 20, blank = True, null = True)

User.profile = property(lambda u: EntProfile.objects.get_or_create(user = u) [0])
'''

class Venture(models.Model):
	# Page 1
	user = models.ForeignKey(User)
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
	creation_date = models.DateField(auto_now = False, auto_now_add = True)

	def __unicode__(self, ):
		return self.name


		#generate random key
		#http://stackoverflow.com/questions/3928016/django-auto-generating-unique-model-fields-and-recursively-calling-auto-generat