import datetime
from django.db import models
from django.contrib.auth.models import User






class Profile(models.Model):
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
    user = models.ForeignKey(User, verbose_name=('user'), related_name='user_mentor')
    applicant = models.CharField(verbose_name='Name of the applicant' , max_length = 100)
    venture_name = models.CharField(verbose_name='Name of the Venture' , max_length = 200)
    unique_id = models.CharField(verbose_name='Unique nickname for the venture ', max_length = 10,  blank = True)
    industry = models.CharField(verbose_name='Industry ', max_length = 200)
    website = models.URLField(verbose_name='Website (if any)', blank = True, null = True)
    legally_formed = models.BooleanField(verbose_name='Is it legally formed? ', default = False)
    other_team_members = models.CharField(verbose_name='Other Team Members', blank = True, null = True, max_length = 200)
    project_leader = models.BooleanField(verbose_name='Are you the project leader? ', default = True)
    chracterstics = models.TextField(verbose_name='Chracterstics of the company ', blank = True, null = True,)
    skills_lacking = models.TextField(verbose_name='What skills are you lacking? ', blank = True, null = True,)
    # Page 2
    target_customers = models.TextField(verbose_name='Who is the targeted customer? ', blank = True, null = True,)
    needs_satisfied = models.TextField(verbose_name='What niche or need will the service satisfy? ', blank = True, null = True,)
    competitors = models.TextField(verbose_name='Who are the (possible) competitors? ', blank = True, null = True,)
    free_alternatives = models.TextField(verbose_name='Are there any free alternatives currently? ', blank = True, null = True,)
    # Page 3
    how_meets_customer_needs = models.TextField(verbose_name="How does it meet the customer's needs? ", blank = True, null = True,)
    how_differentiate = models.TextField(verbose_name='How does it differentiate from the current market? ', blank = True, null = True,)
    describe_mvp = models.TextField(verbose_name='Please describe the Minimal Viable Product (MVP) ', blank = True, null = True,) #mvp = minimal viable product
    #Page 4
    launch_date = models.DateField(verbose_name='When is the projected launch date? ', auto_now = False, auto_now_add = False, null = True, blank = True)
    investment_needed = models.TextField(verbose_name='How much investment is needed? ', blank = True, null = True,)
    created = models.DateTimeField(auto_now = True, auto_now_add = True)
    #extra
    extra_notes = models.TextField(verbose_name='Notes ', blank = True, null = True, )

    class Meta:
        ordering = ["-created"]

    def __unicode__(self, ):
        return unicode(self.venture_name)





