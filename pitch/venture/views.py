from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import CreateView, ListView, UpdateView

from venture.forms import VentureForm
from venture.models import Venture
from venture.models import Profile as EntProfile

from mentor.models import Mentor_Venture


#Ent = Entrepreneur
#Men = Mentor


class VentureListView(ListView):
    '''
    outputs list of their ventures to entrepreneurs
    '''
    model = Venture
    template_name = 'venture/ventures_all.html'

    @method_decorator(login_required)
    def get_queryset(self):
        return Venture.objects.filter(user= self.request.user)
    
    @method_decorator(login_required)
    def get_context_data(self, **kwargs):
        context = super(VentureListView, self).get_context_data(**kwargs)
        return context





class VentureCreateView(CreateView):
    '''
    creates new venture for entrepreneurs
    '''
    form_class = VentureForm
    model = Venture
    template_name = 'venture/ventures_add.html'
    success_url = '/ent/ventures/'

    @method_decorator(login_required)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VentureCreateView, self).form_valid(form)





class VentureUpdateView(UpdateView):
    '''
    updates a specific venture
    '''
    form_class = VentureForm
    model = Venture
    template_name = 'venture/ventures_edit.html'
    success_url = '/ent/home/'

    @method_decorator(login_required)
    def get_object(self, queryset=None):
        obj = Venture.objects.get(id=self.kwargs['id'])
        return obj



#actually can be replaced with get_or_create
@login_required
def ent_view_profile(request):
    try:
        obj = EntProfile.objects.get(username = request.user)
        return HttpResponseRedirect("/ent/profile/edit/")
    except ObjectDoesNotExist:
        obj = EntProfile(username = request.user)
        obj.save()
        return HttpResponseRedirect("/ent/profile/edit/")




class Ent_Edit_Profile(UpdateView):
    '''
    Need a query set to use updateview. Mentor_View_Profile will create
    a query if Mentor Profile Model is empty. 
    '''
    model = EntProfile
    template_name = 'venture/profiles.html'
    fields = ['dob', 'state_residency', 'city_residency', 'state_office' , 'city_office'] 
    success_url = '/ent/profile/edit/'

    @method_decorator(login_required)
    def get_object(self, queryset = None):
        return EntProfile.objects.get(username = self.request.user)

    @method_decorator(login_required)
    def form_valid(self, form):
        form.username = self.request.user
        form.save()
        return super(Ent_Edit_Profile, self).form_valid(form)







class VentureApplicationView(VentureListView):
    '''
    lists all the ventures
    '''
    model = Venture
    template_name = 'venture/ventures_applications.html'

    @method_decorator(login_required)
    def get_queryset(self):
        return Venture.objects.filter(user= self.request.user)
    
    @method_decorator(login_required)
    def get_context_data(self, **kwargs):
        context = super(VentureApplicationView, self).get_context_data(**kwargs)
        return context







@csrf_exempt
def all_ventures(request):
    user = request.user
    the_json = serializers.serialize('json',
                Venture.objects.filter(user = user),
                indent=2, use_natural_keys=True)
    return HttpResponse(the_json)








@csrf_exempt
def apply_ventures(request):
    if request.method == 'POST':
        #applicant
        applicant = request.user
        #mentor
        mentor_name = request.POST['mentor_name']
        mentor = request.POST['mentor_username']
        mentor_username = User.objects.get(username = mentor)
        #venture
        chosen_venture = request.POST['chosen_venture']
        try:
            venture = Venture.objects.get(user = applicant, venture_name = chosen_venture)
            check_duplicate = Mentor_Venture.objects.filter(user = mentor_username,
                                        unique_id = venture.unique_id)   
            if check_duplicate.exists():
                return HttpResponse("A duplicate application exists")
            else:
                form = Mentor_Venture(user = mentor_username, applicant = unicode(venture.user),
                    venture_name = venture.venture_name, unique_id = venture.unique_id,
                    industry = venture.industry)
                form.save()
                return HttpResponse("Application sent. Thank you.")
        except:
            return HttpResponse("Something went wrong")
                
               
