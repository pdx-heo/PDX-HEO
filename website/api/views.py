from website.models import Organization, Shelter
from .serializers import OrganizationSerializer
from rest_framework import generics

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
  """
    Create get,post, put, delete organization
  """
  queryset = Organization.objects.all()
  serializer_class = OrganizationSerializer


class OrganizationList(generics.ListCreateAPIView):

  """
  List all organizations or create a new organization
  """
  queryset = Organization.objects.all()
  serializer_class = OrganizationSerializer
