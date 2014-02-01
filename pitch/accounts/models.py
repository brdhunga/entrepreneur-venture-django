from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from userena.models import UserenaBaseProfile


class UserType(UserenaBaseProfile):
    '''
    Add custom model usertype, and other fields to base userena profile
    '''
    user = models.OneToOneField(User,unique=True,
                                    verbose_name=_('user'),
                                    related_name='my_profile')
    usertype = models.CharField(max_length=3,
                                    default = 'Ent')
    dob = models.DateField(verbose_name='State of Residency: ',
                                    blank = True, null = True)
    state_of_residency = models.CharField(verbose_name='State of Residency: ',
                                    max_length = 25, blank = True,
                                    null = True)
    city_of_residency = models.CharField(verbose_name='City of Residency: ',
                                    max_length = 25,
                                    blank = True, null = True)
    state_of_office = models.CharField(verbose_name='State of Office: ',
                                    max_length = 25,
                                    blank = True, null = True)
    city_of_office = models.CharField(verbose_name='City of Residency: ',
                                    max_length = 25,
                                    blank = True, null = True)
