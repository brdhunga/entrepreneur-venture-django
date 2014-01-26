from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect, render
from accounts.models import UserType
from django.core.exceptions import ObjectDoesNotExist


'''
Check the type of the user and redirect as required.
A custom decorator might be better
'''
def usertype_check(request):
    if request.user.is_authenticated():
        user = request.user
        print user
        try:
            user = UserType.objects.get(user = user)
            if user.usertype == "Ent":
                print user.usertype
                return HttpResponseRedirect('/ent/home/')
            elif user.usertype == "Men":
                return HttpResponseRedirect('/mentor/home/')
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/home/')