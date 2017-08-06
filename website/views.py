from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Service
from .models import Organization
from .models import Testimony


# Create your views here.
def index(request):
  return render(request, 'website/index.html')


def safetymap(request):
  return render(request, 'website/safetymap.html')


def communityboard(request):
  return render(request, 'website/communityboard.html')


def testimonials(request):
    context = RequestContext(request)
    #get list of 10 testimonials and place in dict that gets displayed by template
    testimonials_list = Testimony.objects.order_by('title')[:10]
    context_dict = {'testimonials': testimonials_list}
    #Render response and send it back
    return render_to_response('website/testimonials.html', context_dict, context)


def about(request):
  return render(request, 'website/about.html')


class FinderView(generic.ListView):
  template_name = 'website/finder.html'
  context_object_name = 'service_list'

  def get_queryset(self):
    return Service.objects.order_by('name')[:10]


class OrganizationView(generic.DetailView):
  model = Organization
  template_name = 'website/organization.html'


class ServiceView(generic.DetailView):
  model = Service
  template_name = 'website/service.html'
