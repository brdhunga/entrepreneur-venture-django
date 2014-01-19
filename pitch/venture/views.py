from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
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
    success_url = '/ent/ventures/'

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


class VentureApplicationView(ListView):
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
    the_json = serializers.serialize('json', Venture.objects.filter(user = user), indent=2, use_natural_keys=True)
    print "all the ventures are"
    print the_json
    return HttpResponse(the_json)