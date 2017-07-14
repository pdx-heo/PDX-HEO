from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from website.models import Organization, Shelter
from .serializers import OrganizationSerializer

class OrganizationDetail(APIView):
  """
  """
  def get_object(self, pk):
      try:
          return Organization.objects.get(pk=pk)
      except Organization.DoesNotExist:
          raise Http404

  def get(self, request, pk, format=None):
    organization = self.get_object(pk)
    serializer = OrganizationSerializer(organization)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    organization = self.get_object(pk)
    serializer = OrganizationSerializer(organization, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    organization = self.get_object(pk)
    organization.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# example: http://127.0.0.1:8000/organizations.json  # JSON suffix
# example http://127.0.0.1:8000/organizations.api   # Browsable API suffix
class OrganizationList(APIView):
  """
  List all organizations or create a new organization
  """
  def get(self, request, format=None):
      organizations = Organization.objects.all()
      serializer = OrganizationSerializer(organizations, many=True)
      return Response(serializer.data)

  def post(self, request, format=None):
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
