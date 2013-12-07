from django.views.generic import CreateView, ListView, UpdateView
from venture.forms import VentureForm
from venture.models import Venture


class VentureListView(ListView):
    model = Venture
    template_name = 'venture/ventures_all.html'

    def get_queryset(self):
        return Venture.objects.filter(user= self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(VentureListView, self).get_context_data(**kwargs)
        return context

class VentureCreateView(CreateView):
    form_class = VentureForm
    model = Venture
    template_name = 'venture/ventures_add.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VentureCreateView, self).form_valid(form)


class VentureUpdateView(UpdateView):
    form_class = VentureForm
    model = Venture
    template_name = 'venture/ventures_edit.html'
    success_url = '/ent/home/'

    def get_object(self, queryset=None):
        obj = Venture.objects.get(id=self.kwargs['id'])
        return obj

