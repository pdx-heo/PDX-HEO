from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Shelter
from .models import Organization


def index(request):
    return render(request, 'pdxheo/index.html')

def safetymap(request):
    return render(request, 'pdxheo/safetymap.html')

def communityboard(request):
    return render(request, 'pdxheo/communityboard.html')

def testimonies(request):
    return render(request, 'pdxheo/testimonies.html')

def about(request):
    return render(request, 'pdxheo/about.html')

def finder(request):
    shelter_list = Shelter.objects.order_by('name')[:10]
    context = {'shelter_list': shelter_list}
    return render(request, 'pdxheo/finder.html', context)

def organization(request, organization_id):
    org = get_object_or_404(Organization, pk=organization_id)
    return render(request, 'pdxheo/organization.html', {'organization': org})

def shelter(request, shelter_id):
    she = get_object_or_404(Shelter, pk=shelter_id)
    return render(request, 'pdxheo/shelter.html', {'shelter': she})
