from django.conf import settings
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.FloatField()
    running_time = models.IntegerField(default=0)
    review_text = models.TextField()
    director = models.CharField(max_length=100,default='Unknown')
    main_actor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title  # Django 관리 인터페이스에서 영화 제목이 표시되도록 설정
