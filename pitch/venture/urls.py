from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from venture.views import VentureListView, VentureCreateView, VentureUpdateView,\
                            VentureApplicationView, all_ventures, apply_ventures,\
                            Ent_Edit_Profile, ent_view_profile



urlpatterns = patterns('',
    url(r'^home/$', TemplateView.as_view(template_name="venture/home.html"), name = "ent_home"),
    url(r'^profile/$', ent_view_profile, name = "ent_profile"),
    url(r'^profile/edit/$', Ent_Edit_Profile.as_view(), name = "ent_profile_edit"),
    url(r'^ventures/add/$', VentureCreateView.as_view(), name = "venture_add"),
    url(r'^ventures/$', VentureListView.as_view(), name='venture_list'),
    url(r'^ventures/edit/(?P<id>[\w-]+)$', VentureUpdateView.as_view(), name = 'venture_edit'),
    url(r'^ventures/application/$', VentureApplicationView.as_view(), name = 'venture_application'),
    url(r'^all_ventures/$', all_ventures, name='all_ventures'),
    url(r'^apply/', apply_ventures , name = 'apply_ventures'),
)

#url( r'^blogs/(?P<post_slug>[-a-zA-Z0-9]+)/?$', 'blog.views.single_blog', name = 'single_blog'),