from django import forms
from .models import *

class StackForm(forms.ModelForm):
    
    class Meta:
        model = Stack
        fields = "__all__"

        labels = {
            'image':'image url'
        }

        widgets = {
            'title':forms.TextInput(attrs={'autocomplete':'new-password', 'autofocus':True}),
            'text':forms.Textarea(attrs={'style':'resize:none;', 'cols':30, 'autocomplete':'new-password'}),
            'image_url':forms.TextInput(attrs={'autocomplete':'new-password'})
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['text']

        widgets = {
            'text':forms.Textarea(attrs={'style':'resize:none;', 'rows':3, 'autocomplete':'new-password'})
        }


class TopicFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput())