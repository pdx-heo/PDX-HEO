"""
MIT License
Copyright (c) 2017 Mackenzie Wangenstein, Chitra Maruthavanan, Andy Mayer


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from . import views


testimonials_list = views.TestimonyViewSet.as_view({
    'get':'list',
    'post': 'create'
})


testimonials_detail = views.TestimonyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

service_list = views.ServiceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

service_detail = views.ServiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'

})

testimonials_list = views.TestimonyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

Testimony_detail = views.TestimonyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'

})
#
organization_list = views.OrganizationViewSet.as_view({
'get': 'list',
'post': 'create'
})

organization_detail = views.OrganizationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'

})

user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})



urlpatterns = [
  url(r'^$', views.api_root),
  url(r'^users/$', user_list, name='user-list'),
  url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user'),
  url(r'^organization/$', organization_list, name='organization-list'),
  url(r'^organization/(?P<pk>[0-9]+)/$', organization_detail, name='organization'),
  url(r'^service/$', service_list, name='service-list'),
  url(r'^service/(?P<pk>[0-9]+)/$', service_detail, name='service'),
  url(r'^Testimony/$', testimonials_list, name='testimonials_list'),
  url(r'^Testimony/(?P<pk>[0-9]+)/', testimonials_detail, name='testimony'),
]

#
urlpatterns = format_suffix_patterns(urlpatterns)
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
