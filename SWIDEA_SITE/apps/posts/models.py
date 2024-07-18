from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField('아이디어명', max_length=24)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d',null=True)
    detail = models.CharField('아이디어 설명',max_length =100, default='')
    inter = models.CharField('아이디어 관심도',max_length=24, default='')
    tool = models.CharField('예상 개발 툴',max_length=24,default='python')
    

    def __str__(self):
        return self.title