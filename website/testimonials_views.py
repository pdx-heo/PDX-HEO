from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TestimonyForm
from django.shortcuts import get_object_or_404
#
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#
from django.urls import reverse_lazy
from .models import Testimony

class TestimonyDetail(DetailView):
    """
        generic class based detail view for Testimony
    """
    model = Testimony
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TestimonyDetail, self).form_valid(form)

class TestimonyCreate(CreateView):
    model = Testimony
    fields = ['author', 'story', 'author']
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TestimonyCreate, self).form_valid(form)

class TestimonyUpdate(UpdateView):
    model = Testimony
    fields = ['author', 'story', 'author']
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TestimonyUpdate, self).form_valid(form)


class TestimonyDelete(DeleteView):
    model = Testimony
    success_url = reverse_lazy('thanks')

def get_thanks(request):
    return render(request, 'website/thanks.html')

#to do -- follow form set https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
def get_testimony(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestimonyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # testimony_inst = Testimony.objects.get(pk)
            # testimony_inst.title = form.cleaned_data['title']
            # testimony_inst.story = form.cleaned_data['story']
            # testimony_inst.author = form.cleaned_data['author']
            # testimony_inst.save()

            #redirect to new url
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestimonyForm()

    return render(request, 'website/testimonials.html', {'form': form})
