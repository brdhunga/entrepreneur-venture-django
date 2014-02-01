from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm
from accounts.models import UserType



class SignupFormExtra(SignupForm):
    '''
    Overriding the default userena signup form to 
    include usertype = Ent (entreprenuer), or Mentor(Men)
    '''
    usertype = forms.CharField(label=_(u'user_type'),max_length=3,required=True)
    
    def save(self):
        '''
        get usertype field from registration form
        and assigns its values to usertype field in userrena 
        '''
        user = super(SignupFormExtra, self).save()
        user_profile = user.get_profile()
        usertype = self.cleaned_data['usertype']
        user_profile.usertype = usertype
        user_profile.save()
        return user

