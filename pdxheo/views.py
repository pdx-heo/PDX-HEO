from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Service
from .models import Organization


def index(request):
    service_list = Service.objects.order_by('name')[:10]
    context = {'service_list': service_list}
    return render(request, 'pdxheo/index.html', context)


def organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    return render(request, 'pdxheo/organization.html', {'organization': organization})


def service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'pdxheo/service.html', {'service': service})

