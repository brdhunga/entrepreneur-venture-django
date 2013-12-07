from django.conf.urls import patterns, include, url
from django.conf import settings
from django.core.context_processors import csrf
#Generic class views
from django.views.generic import TemplateView
from accounts.forms import SignupFormExtra


#import Views from Apps
from home import views
from profiles.views import EntProfileUpdateView
from home.views import TemplateViewWithContext

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Static pages
    (r'^$', TemplateViewWithContext.as_view(template_name="main/home.html", extra_context = {'current' : 'home'})),
    (r'^services/', TemplateViewWithContext.as_view(template_name="main/services.html", extra_context = {'current' : 'services'})),
    (r'^price/', TemplateViewWithContext.as_view(template_name="main/price.html", extra_context = {'current' : 'pricing'})),



    #url(r'^accounts/register/$', CustomRegistrationView.as_view(form_class=CustomRegistrationForm)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #user-registration
    (r'^accounts/signup/$','userena.views.signup', {'signup_form': SignupFormExtra}),
    (r'^accounts/', include('userena.urls')),

    #account profile
    (r'^ent/', include('venture.urls')),

    #usercheck for now, add a decorator later
    url(r'^usercheck/', 'accounts.views.usertype_check', name = 'usertype_check' ),

    #mentor home
    (r'^mentor/home/', TemplateView.as_view(template_name="mentor/mentor_home.html")),


)
