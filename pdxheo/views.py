from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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


class FinderView(generic.ListView):
  template_name = 'pdxheo/finder.html'
  context_object_name = 'shelter_list'

  def get_queryset(self):
    return Shelter.objects.order_by('name')[:10]


class OrganizationView(generic.DetailView):
  model = Organization
  template_name = 'pdxheo/organization.html'


class ShelterView(generic.DetailView):
  model = Shelter
  template_name = 'pdxheo/shelter.html'


def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('index')
  else:
    form = UserCreationForm()
  return render(request, 'pdxheo/register.html', {'form': form})
