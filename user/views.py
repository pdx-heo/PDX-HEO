from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
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
  return render(request, 'user/register.html', {'form': form})