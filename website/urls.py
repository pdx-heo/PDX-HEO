"""
MIT License
Copyright (c) 2017 Mackenzie Wangenstein, Chitradevi Maruthavanan, Andy Mayer


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


from django.conf.urls import url, include

from . import views
from . import testimonials_views
from django.conf import settings
#from django.conf import django.views

urlpatterns = [
  # ex: /pdxheo/
  url(r'^$', views.index, name='index'),
  url(r'^about/$', views.about, name='about'),
  url(r'^community/$', views.communityboard, name='community_board'),
  url(r'^finder/$', views.finder, name='finder'),
  url(r'^safety/$', views.safetymap, name='safety_map'),
  url(r'^testimonials/$', views.testimonials, name='testimonials'),
  url(r'^testimonials/(?P<pk>\d+)$', testimonials_views.TestimonyDetail.as_view(), name='testimonials_detail'),
  url(r'^testimonials/create', testimonials_views.TestimonyCreate.as_view(), name='testimony_create'),
  url(r'^testimonials/(?P<pk>\d+)/update/$', testimonials_views.TestimonyUpdate.as_view(), name='testimony_update'),
  url(r'^testimonials/(?P<pk>\d+)/delete/$', testimonials_views.TestimonyDelete.as_view(), name='testimony_delete'),
  url(r'^thanks', testimonials_views.get_thanks, name='thanks'),
  # ex: /pdxheo/organization/1/
  url(r'^organization/(?P<pk>[0-9]+)/$', views.OrganizationView.as_view(), name='organization_detail'),
  # ex: /pdxheo/shelter/1/
  url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceView.as_view(), name='service_detail'),
  url(r'^api/', include('website.api.urls', namespace="api")),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
