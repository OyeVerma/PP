from django import forms
from .models import *

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = "__all__"

        labels = {
            'image':'image url'
        }

        widgets = {
            'title':forms.TextInput(attrs={'autocomplete':'new-password'}),
            'text':forms.Textarea(attrs={'style':'resize:none;', 'cols':30, 'autocomplete':'new-password'}),
            'image_url':forms.TextInput(attrs={'autocomplete':'new-password'})
        }

class TopicFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput())