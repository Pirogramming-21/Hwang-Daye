from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'main_actor', 'genre', 'rating', 'running_time', 'review_text', 'release_year']