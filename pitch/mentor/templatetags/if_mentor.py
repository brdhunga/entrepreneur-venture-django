from django import template
from django.contrib.auth.models import User

register = template.Library()



@register.simple_tag
def if_is_mentor(id):
    return True
    
