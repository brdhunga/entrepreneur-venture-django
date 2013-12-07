from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from venture.views import VentureListView, VentureCreateView, VentureUpdateView


urlpatterns = patterns('',
    url(r'^home/$', TemplateView.as_view(template_name="venture/home.html"), name = "ent_home"),
    url(r'^ventures/add/$', VentureCreateView.as_view(), name = "venture_add"),
    url(r'^ventures/$', VentureListView.as_view(), name='venture_list'),
    url('^ventures/edit/(?P<id>[\w-]+)$', VentureUpdateView.as_view(), name = 'venture_edit'),
)

#url( r'^blogs/(?P<post_slug>[-a-zA-Z0-9]+)/?$', 'blog.views.single_blog', name = 'single_blog'),