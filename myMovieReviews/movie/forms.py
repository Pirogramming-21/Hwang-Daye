from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title','release_year', 'genre', 'rating','running_time','review_text','director','main_actor']
        labels = {
            'title': '제목',
            'release_year': '개봉년도',
            'genre': '장르',
            'rating': '별점',
            'running_time': '러닝타임',
            'review_text': '리뷰',
            'director': '감독',
            'main_actor': '배우',
        }