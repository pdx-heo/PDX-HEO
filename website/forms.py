from django import forms
from django.forms import ModelForm

from .models import Testimony


# class TestimoniesForm(forms.Form):
#     title = forms.CharField(label=' title', max_length=150)
    # story = forms.CharField(widget=forms.Textarea)
    # #author = forms.CharField(label='author', max_length=150, required=false)



class TestimoniesForm(ModelForm):
    class Meta:
        model = Testimony
        fields = ['title', 'story', 'author']


#creating a form to add a testimony
form = TestimoniesForm()

#creating a form to chang an existinng testimony
#testimony = Testimony.objects.get(pk=1)
#form = TestimoniesForm(instance=testimony)
