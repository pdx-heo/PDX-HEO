from django import forms

#start with single field example - will expand later.
class TestimoniesForm(forms.Form):
    title = forms.CharField(label='title', max_length=150)
