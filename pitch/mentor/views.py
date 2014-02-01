from django.views.generic.edit import UpdateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


from django.views.generic import CreateView, ListView, UpdateView


from venture.models import Venture
from mentor.models import Profile as MentorProfile
from mentor.models import Mentor_Venture, Profile
from mentor.forms import ProfileForm, Mentor_VentureForm




#check if mentor profile exists, if not create
def mentor_view_profile(request):
    try:
        obj = Profile.objects.get(username = request.user)
        return HttpResponseRedirect("/mentor/profile/edit/")
    except Profile.DoesNotExist:
        obj = Profile(username = request.user, address = "123 Street")
        obj.save()
        return HttpResponseRedirect("/mentor/profile/edit")




#edit mentor profile
class Mentor_Edit_Profile(UpdateView):
    '''
    Need a query set to use updateview. Mentor_View_Profile will create
    a query if Mentor Profile Model is empty. 
    '''
    model = Profile
    template_name = 'mentor/mentor_profile.html'
    fields = ['name', 'address', 'zipcode'] 
    success_url = '/mentor/profile/edit'

    def get_object(self, queryset = None):
        return Profile.objects.get(username = self.request.user)

    def form_valid(self, form):
        form.username = self.request.user
        form.save()
        return super(Mentor_Edit_Profile, self).form_valid(form)




class Mentor_List_Applications(ListView):
    '''
    outputs list of all ventures copy that belongs to an entrepreneur
    '''
    model = Mentor_Venture
    template_name = 'mentor/mentor_applications.html'

    def get_queryset(self):
        return Mentor_Venture.objects.filter(user= self.request.user)





class Mentor_List_Applicants(ListView):
    '''
    outputs list of all unique applicants copy that have applied to a mentor
    '''
    paginate_by = 20
    model = Mentor_Venture
    template_name = 'mentor/mentor_applicants.html'

    def get_queryset(self):
        all_obj = Mentor_Venture.objects.filter(user = self.request.user)
        obj = all_obj.values().distinct()
        return obj






class Mentor_Venture_Edit(UpdateView):
    '''
    Need a query set to use updateview. Mentor_View_Profile will create
    a query if Mentor Profile Model is empty. 
    '''
    form_class = Mentor_VentureForm
    template_name = 'mentor/mentor_update.html'
    success_url = '/mentor/home/'


    def get_object(self):
        self.id = self.kwargs['id']
        obj = get_object_or_404(Mentor_Venture.objects.filter(user = self.request.user, unique_id = self.id))
        return obj







@csrf_exempt
def mentor(request):
    if request.method == 'POST':
        print "the post"
        print request.POST['title']
        data = serializers.serialize('json', Venture.objects.filter(user = request.user))
        print "the json is"
        print data
        return HttpResponse(data)
    else:
        return render(request, "exp_template.html", {"name":name})





@csrf_exempt
def mentor_search(request):
    the_json = serializers.serialize('json', MentorProfile.objects.all(), indent=2, use_natural_keys=True)
    return HttpResponse(the_json)



def mentor_venture_edit(request, id):
    return HttpResponse(id)







