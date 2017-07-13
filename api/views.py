from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from website.models import Organization, Shelter
from .serializers import OrganizationSerializer


# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
def organization(request, organization_id, format=None):
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


# example: http://127.0.0.1:8000/organizations.json  # JSON suffix
# example http://127.0.0.1:8000/organizations.api   # Browsable API suffix
@api_view(['GET', 'POST'])
def organization_list(request, format=None):
  """
  List all organizations or create a new organization
  """
  if request.method == 'GET':
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    # data = JSONParser().parse(request)
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # return JsonResponse(serializer.data, status=201)
    # return JsonResponse(serializer.errors, status=400)
