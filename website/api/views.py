from website.models import Organization, Service
from .serializers import OrganizationSerializer, ServiceSerializer, UserSerializer
from rest_framework import generics, permissions

from django.contrib.auth.models import User #TODO - change to user in project when re-introduced


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
      Create get,post, put, delete organization
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ServiceList(generics.ListCreateAPIView):
    """
    List all organizations or create a new organization
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        serializer.save(creator=self.request.user)
