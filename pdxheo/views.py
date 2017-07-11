from django.shortcuts import get_object_or_404, render
from django.http import Http404
#HttpResponse,HttpResponseRedirect,
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import generic
#remove?
#from django.views.decorators.csrf import csrf_exempt
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


class FinderView(generic.ListView):
  template_name = 'pdxheo/finder.html'
  context_object_name = 'shelter_list'

  def get_queryset(self):
    return Shelter.objects.order_by('name')[:10]


class OrganizationView(generic.DetailView):
  model = Organization
  template_name = 'pdxheo/organization.html'

@api_view(['GET','PUT','DELETE'])
def organization(request, organization_id, formate=None):
    #old version

    #org = get_object_or_404(Organization, pk=organization_id)
    #return render(request, 'pdxheo/organization.html', {'organization': org})

    #new version

    try:
        organization = Organization.objects.get(organization_id=organization_id)
    except Organization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = OrganizationSerializer(organization)
            return Response(serializer.data)

        elif request.method == 'PUT':
             serializer = OrganizationSerializer(organization, data=request.data)
             if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            organization.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# example: http://127.0.0.1:8000/organization.json  # JSON suffix
# example http://127.0.0.1:8000/organization.api   # Browsable API suffi
@api_view(['GET','POST'])
def organization_list(request, format=None):
    """
    List all organizations or create a new organizatoin
    """
    if request.method == 'GET':
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
    #    data = JSONParser().parse(request)
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    #return JsonResponse(serializer.data, status=201)
            #    return JsonResponse(serializer.errors, status=400)


class ShelterView(generic.DetailView):
  model = Shelter
  template_name = 'pdxheo/shelter.html'
