from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from .views import OrganizationViewSet, ServiceViewSet, api_root

#TODO: introuce binding-viewsets-to-urls-explicitly
#http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#binding-viewsets-to-urls-explicitly
urlpatterns = [
  url(r'^$', api_root),
  #url(r'^users/$', views.UserList.as_view(), name='user-list'),
#  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user'),
  #url(r'^organization/$', views.OrganizationList.as_view(), name='organization-list'),
 # url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationDetail.as_view(), name='organization'),
 # url(r'^service/$', views.ServiceList.as_view(), name='service-list'),
  #url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view(), name='service'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
