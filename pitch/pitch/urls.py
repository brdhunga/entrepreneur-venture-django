from django.conf import settings
from django.conf.urls import patterns, include, url
from django.core.context_processors import csrf

# admin
from django.contrib import admin
admin.autodiscover()

# Generic class views
from django.views.generic import TemplateView

# import Views from Apps
from accounts.forms import SignupFormExtra



urlpatterns = patterns('',

    #static pages
    url(r'^$', TemplateView.as_view(template_name="main/home.html") , name = 'home'),
    url(r'^services/', TemplateView.as_view(template_name="main/services.html"), name = 'services'),
    url(r'^price/', TemplateView.as_view(template_name="main/price.html"), name = 'price'),

    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #user-registration
    (r'^accounts/signup/$','userena.views.signup', {'signup_form': SignupFormExtra}),
    (r'^accounts/', include('userena.urls')),

    #  venture app, which lets entreprenuers fill venture and apply to mentors
    (r'^ent/', include('venture.urls')),

    # mentor profile, which lets mentors see applications received and applicants
    (r'^mentor/', include('mentor.urls')),

    #experiment
    #url(r'^exp/$', try2),

    # possibly replace with a decorator: redirects based on whether the user is mentor or entrepreneur
    url(r'^usercheck/', 'accounts.views.usertype_check', name = 'usertype_check' ),

)
