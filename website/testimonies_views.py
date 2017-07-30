from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TestimoniesForm

def get_title(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestimoniesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestimoniesForm()

                #TODO consider replacing with website/testimonies
    return render(request, 'website/testimonies.html', {'form': form})


def get_thanks(request):
    return render(request, 'website/thanks.html')
