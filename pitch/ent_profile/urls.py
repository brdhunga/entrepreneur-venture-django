from django.conf.urls import patterns, include, url
from .views import ent_profile

urlpatterns = patterns('',
    url(r'^profile/$', 'ent_profile.views.ent_profile'),
    url(r'^home/$', 'ent_profile.views.home'),
    url(r'^ventures/add/$', 'ent_profile.views.add_venture'),
    url(r'^ventures/$', 'ent_profile.views.all_ventures'),
    url(r'^ventures/(?P<nickname1>[-a-zA-Z0-9]+)/edit', 'ent_profile.views.edit_venture'),
)

#url( r'^blogs/(?P<post_slug>[-a-zA-Z0-9]+)/?$', 'blog.views.single_blog', name = 'single_blog'),