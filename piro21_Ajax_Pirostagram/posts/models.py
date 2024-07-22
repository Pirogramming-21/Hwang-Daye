from django.db import models

# Create your models here.
class Post (models.Model):
    content = models.TextField('내용',max_length=100)
    like = models.IntegerField('좋아요',default=0)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)