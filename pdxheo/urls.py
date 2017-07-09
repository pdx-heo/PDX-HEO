from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /pdxheo/
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),

    url(r'^communityboard', views.communityboard, name='communityboard'),
    url(r'^community', views.communityboard, name='communityboard'),

    url(r'^finder', views.finder, name='finder'),

    url(r'^safetymap', views.safetymap, name='safetymap'),
    url(r'^safety', views.safetymap, name='Safety Map'),

    url(r'^testimonies', views.testimonies, name='testimonies'),

    # ex: /pdxheo/organization/1/
    url(r'^organization/(?P<organization_id>[0-9]+)/$', views.organization, name='organization'),

    # ex: /polls/service/1/
    url(r'^shelter/(?P<shelter_id>[0-9]+)/$', views.shelter, name='shelter'),
]
