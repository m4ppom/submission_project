from django import forms
from .models import Movie, Comment 

class MovieModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=200)

    class Meta:
        model = Movie
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=100)
    comment_score = forms.CharField(min_length=2, max_length=100)
    class Meta:
        model = Comment
        fields = ('content', 'comment_score', )
