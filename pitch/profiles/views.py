from django.views.generic import CreateView, ListView, UpdateView

from profiles.forms import ProfileDetailForm
from profiles.models import ProfileDetail


'''
UpdatView to update Enreprenuer's account profile
'''
class EntProfileUpdateView(UpdateView):
    form_class = ProfileDetailForm
    model = ProfileDetail
    template_name = 'venture/profiles.html'
    success_url = '/thanks/'

    def get_object(self, queryset=None):
    	return self.request.user

    def form_valid(self, form):
        clean = form.cleaned_data 
        form.user = self.request.user
        context = {} 
        return super(EntProfileUpdateView, self).form_valid(form)
        #super(EntProfileUpdateView, self).save(form)

