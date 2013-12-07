from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .forms import  VentureForm
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
	user = request.user
	return render_to_response('ent_profile/ent_home.html', RequestContext(request, {
        'user' : user,
    }))


@login_required
def ent_profile(request):
	if request.method == "POST":
		form = EntProfileForm(request.POST, instance = request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ent/profile/')
	else:
		user = request.user
		profile = user.profile
		form = EntProfileForm(instance = profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('ent_profile/profile.html', args)


@login_required
def add_venture(request):
    form = VentureForm
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('ent_profile/add_venture.html', args)

@login_required
def all_ventures(request):
    owner = request.user
    all_ventures = Venture.objects.filter(user = owner)
    return render_to_response('ent_profile/list_ventures.html', RequestContext(request, {
    'all_ventures' : all_ventures,
    })) 

@login_required
def edit_venture(request, nickname1):
    user = request.user
    inst = Venture.objects.get(nickname = nickname1)
    form = VentureForm(instance = inst)
    return render_to_response('ent_profile/edit_ventures.html', {'form':form})