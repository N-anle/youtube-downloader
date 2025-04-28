from django import forms
from django.forms import TextInput

class VideoForm(forms.Form):
   url = forms.URLField(
      label= 'url',
      widget=TextInput(
         attrs={
            'class' : 'input',
            'placeholder' : 'Input Youtube video url'
         }
      )
   )