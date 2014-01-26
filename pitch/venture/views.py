from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import CreateView, ListView, UpdateView

from venture.forms import VentureForm
from venture.models import Venture
from mentor.models import Mentor_Venture
from venture.models import Profile as EntProfile


#Ent = Entrepreneur


class VentureListView(ListView):
    '''
    outputs list of all ventures to entrepreneurs
    '''
    model = Venture
    template_name = 'venture/ventures_all.html'

    def get_queryset(self):
        return Venture.objects.filter(user= self.request.user)
    
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

    def get_object(self, queryset=None):
        obj = Venture.objects.get(id=self.kwargs['id'])
        return obj





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

    def get_object(self, queryset = None):
        return EntProfile.objects.get(username = self.request.user)

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

    def get_queryset(self):
        return Venture.objects.filter(user= self.request.user)
    
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
        mentor_username = User.objects.filter(username = mentor)
        #venture
        chosen_venture = request.POST['chosen_venture']
        venture = Venture.objects.filter(user = applicant, venture_name = chosen_venture)
        if venture.exists():
            check_duplicate = Mentor_Venture.objects.filter(user = mentor_username[0],
                unique_id = venture[0].unique_id)
            if not check_duplicate.exists:                
                venture = venture[0]
                form = Mentor_Venture(user = mentor_username[0] , applicant = unicode(venture.user),
                    venture_name = venture.venture_name, unique_id = venture.unique_id,
                    industry = venture.industry)

                form.save()
                return HttpResponse("Works")
            else:
                return HttpResponse("Duplicate Exists")
        else:
            return HttpResponse("Does not work")
                
               
