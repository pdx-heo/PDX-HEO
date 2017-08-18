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


from django import forms
from django.forms import ModelForm
from .models import Testimony
from rest_framework import serializers

class TestimonyForm(ModelForm):
    def clean_title(self):
        data = self.cleaned_data['title']
        return data;

    def clean_story(self):
        data = self.cleaned_data['story']
        return data;

    def clean_author(self):
        data = self.cleaned_data['author']
        return data;

    def clean_image(self):
        data = self.cleaned_data['image']
        return data;

    class Meta:
        model = Testimony
        fields = ['title', 'story', 'author']



#creating a form to add a testimony
#form = TestimonyForm()

#creating a form to chang an existinng testimony
#testimony = Testimony.objects.get(pk=2)
# form = TestimonyForm(instance=testimony)

#class TestimonySerializer(FormSer)
