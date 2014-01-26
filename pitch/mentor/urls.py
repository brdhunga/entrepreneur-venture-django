from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import mentor_view_profile, Mentor_Edit_Profile, mentor_search,\
					Mentor_List_Applications, Mentor_Venture_Edit, Mentor_List_Applicants



urlpatterns = patterns('',
    url(r'^home/$', TemplateView.as_view(template_name="mentor/mentor_home.html"), name = 'mentor_home'),
    url(r'^profile/$', mentor_view_profile, name = 'mentor_profile',),
    url(r'^profile/edit/$', Mentor_Edit_Profile.as_view(), name = 'Mentor_Edit_Profile'),
    url(r'^applications/$', Mentor_List_Applications, name = 'mentor_list_applications'),
    url(r'^applicants/$', Mentor_List_Applicants, name = 'mentor_list_applicants'),
    url(r'^search/$', mentor_search, name = 'mentor_search'),
    url(r'^edit/(?P<id>\w+)', Mentor_Venture_Edit.as_view(), name = 'mentor_venture_edit'),

 )