from django import forms
from .models import Celeb


class CelebForm(forms.ModelForm):
    class Meta:
        model = Celeb
        fields = '__all__'
        
