from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

#potentially remove
from django.template import loader
from django.views import generic

from .models import Shelter
from .models import Organization
from .serializers import OrganizationSerializer

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


class FinderView(generic.ListView):
  template_name = 'pdxheo/finder.html'
  context_object_name = 'shelter_list'

  def get_queryset(self):
    return Shelter.objects.order_by('name')[:10]


class OrganizationView(generic.DetailView):
  model = Organization
  template_name = 'pdxheo/organization.html'

def organization(request, organization_id):
    #old version

    #org = get_object_or_404(Organization, pk=organization_id)
    #return render(request, 'pdxheo/organization.html', {'organization': org})

    #new version

    try:
        organization = Organization.objects.get(organization_id=organization_id)
    except Organization.DoesNotExist:
        return HttpResponse(status=404)


        if request.method == 'GET':
            serializer = OrganizationSerializer(organization)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
             data = JSONParser().parse(request)
             serializer = OrganizationSerializer(organization, data=data)
             if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
             return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            organization.delete()
            return HttpResponse(status=204)


#@csrf_exempt
def organization_list(request):

    if request.method == 'GET':
        print("test")
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrganizationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ShelterView(generic.DetailView):
  model = Shelter
  template_name = 'pdxheo/shelter.html'
