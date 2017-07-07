from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /pdxheo/
    url(r'^$', views.index, name='index'),
    # ex: /pdxheo/organization/1/
    url(r'^organization/(?P<organization_id>[0-9]+)/$', views.organization, name='organization'),
    # ex: /polls/service/1/
    url(r'^shelter/(?P<shelter_id>[0-9]+)/$', views.shelter, name='shelter'),
]
