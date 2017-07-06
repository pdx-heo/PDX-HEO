from django.conf.urls import url
from . import views

app_name = 'pdxheo'
urlpatterns = [
    # ex: /pdxheo/
    url(r'^$', views.index, name='index'),
    # ex: /pdxheo/organization/1/
    url(r'^organization/(?P<organization_id>[0-9]+)/$', views.organization, name='organization'),
    # ex: /polls/service/1/
    url(r'^service/(?P<service_id>[0-9]+)/$', views.service, name='service'),
]
