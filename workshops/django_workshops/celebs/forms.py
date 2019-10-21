from django import forms
from .models import Celeb


class CelebForm(forms.ModelForm):
    class Meta:
        model = Celeb
        fields = '__all__'

class PersonForm(forms.ModelForm):
    age = forms.integerField(validators=[validate_too_old, validate_even])
    class Meta:
        model = Person
        fields = '__all__'