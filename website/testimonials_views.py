"""
MIT License
Copyright (c) 2017 Mackenzie Wangenstein, Chitradevi Maruthavanan, Andy Mayer


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TestimonyForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Testimony

class TestimonyDetail(DetailView):
    """
        generic class based detail view for Testimony
    """
    model = Testimony

class TestimonyCreate(CreateView):
    model = Testimony
    fields = ['title','story','author', 'image']

    def form_valid(self, form):

        if not self.request.user.is_authenticated():
            return HttpResponseForbidden(u'You must be signed in to create a testimony.')
        self.object = form.save(commit=False)
        form.instance.creator = self.request.user
    #if form.data['image']:

        self.object.save()
        return super(TestimonyCreate, self).form_valid(form)

class TestimonyUpdate(LoginRequiredMixin, UpdateView):
    model = Testimony
    fields = ['title','story','author']

    def dispatch(self, request, *args, **kwargs):
        handler = super(TestimonyUpdate, self).dispatch(request, *args, **kwargs)
        # Only allow editing if current user is owner
        if self.object.creator != request.user:
            return HttpResponseForbidden(u'You are not authorized to edit this Testimony.')
        return handler

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TestimonyUpdate, self).form_valid(form)

class TestimonyDelete(DeleteView):
    model = Testimony
    success_url = reverse_lazy('thanks')

    def dispatch(self, request, *args, **kwargs):
        handler = super(TestimonyDelete, self).dispatch(request, *args, **kwargs)
        # Only allow editing if current user is owner
        if self.object.creator != request.user:
            return HttpResponseForbidden(u'You are not authorized to delete this Testimony.')
        return handler

def get_thanks(request):
    return render(request, 'website/thanks.html')
