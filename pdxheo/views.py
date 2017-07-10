from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#from django.template import loader
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


def finder(request):
    shelter_list = Shelter.objects.order_by('name')[:10]
    context = {'shelter_list': shelter_list}
    return render(request, 'pdxheo/finder.html', context)


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

        elif request.method == 'PUT'
             data = JSONParser().parse(request)
             serializer = OrganizationSerializer(organization, data=data)
             if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
             return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            organization.delete()
            return HttpResponse(status=204


@csrf_exempt
def organization_list(request):

    if request.method = 'GET':
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method = 'POST':
        data = JSONParser().parse(request)
        serializer = OrganizationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def shelter(request, shelter_id):
    she = get_object_or_404(Shelter, pk=shelter_id)
    return render(request, 'pdxheo/shelter.html', {'shelter': she})
