from django.conf.urls import url, include

from . import views
from . import testimonies_views

urlpatterns = [
  # ex: /pdxheo/
  url(r'^$', views.index, name='index'),
  url(r'^about/$', views.about, name='about'),
  url(r'^community/$', views.communityboard, name='community_board'),
  url(r'^finder/$', views.FinderView.as_view(), name='finder'),
  url(r'^safety/$', views.safetymap, name='safety_map'),
  url(r'^testimonies/$', views.testimonies, name='testimonies'),
  url(r'^testimonies/title', testimonies_views.get_title, name='testimonies_title'),
  url(r'^thanks',testimonies_views.get_thanks, name='thanks'),
  # ex: /pdxheo/organization/1/
  url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationView.as_view(), name='organization'),
  # ex: /pdxheo/shelter/1/
  url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceView.as_view(), name='service'),
  url(r'^api/', include('website.api.urls', namespace="api")),
]
