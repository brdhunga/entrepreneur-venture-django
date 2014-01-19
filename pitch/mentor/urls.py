from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import mentor_view_profile, Mentor_Edit_Profile, mentor_search



urlpatterns = patterns('',
    url(r'^home/$', TemplateView.as_view(template_name="mentor/mentor_home.html")),
    url(r'^profile/$', mentor_view_profile, name = 'Mentor_View_Profile'),
    url(r'^profile/edit/$', Mentor_Edit_Profile.as_view(), name = 'Mentor_Edit_Profile'),
    url(r'^search/$', mentor_search, name = 'mentor_search'),
    
)

