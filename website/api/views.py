from website.models import Organization, Service
from .serializers import OrganizationSerializer, ServiceSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy

from django.contrib.auth.models import User #TODO - change to user in project when re-introduced
import views

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        #TODO: follow page 6 and 7
        'services': reverse_lazy('api:service-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class ServiceList(generics.ListCreateAPIView):
    """
    List all organizations or create a new organization
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        serializer.save(creator=self.request.user)
