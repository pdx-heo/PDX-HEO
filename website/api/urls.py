from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from . import views

urlpatterns = [
  url(r'^$', views.api_root),
  url(r'^users/$', views.UserList.as_view(), name='user-list'),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user'),
  url(r'^organization/$', views.OrganizationList.as_view(), name='organization-list'),
  url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationDetail.as_view(), name='organization'),
  url(r'^service/$', views.ServiceList.as_view(), name='api.service-list'),
  url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view(), name='service'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
