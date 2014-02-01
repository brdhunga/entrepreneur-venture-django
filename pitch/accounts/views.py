from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect, render
from accounts.models import UserType
from django.core.exceptions import ObjectDoesNotExist



def usertype_check(request):
    '''
    Check the type of the user and redirect as required.
    usertype = men are mentors
    usertype = ent are entrepreneurs
    if usertype not specified return to home
    A custom decorator might be better
    '''
    if request.user.is_authenticated():
        user = request.user
        try:
            user = UserType.objects.get(user = user)
            if user.usertype == "Ent":
                return HttpResponseRedirect('/ent/home/')
            elif user.usertype == "Men":
                return HttpResponseRedirect('/mentor/home/')
            else:
                return HttpResponseRedirect('/') #maybe make a profile not found page
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/ent/home/')