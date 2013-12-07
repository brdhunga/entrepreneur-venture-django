from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect, render
from accounts.models import UserType


'''
Check the type of the user and redirect as required.
A custom decorator might be better
'''
def usertype_check(request):
    if request.user.is_authenticated():
    	user = request.user
    	try:
    		user = UserType.objects.get(user = user)
    		if user.usertype == "Ent":
    			return HttpResponseRedirect('/ent/home/')
    		if user.usertype == "Men":
    			return HttpResponseRedirect('/mentor/home/')
    	except UserType.DoesNotExist:
    		return HttpResponseRedirect('/')