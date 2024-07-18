from django.db import models
# Create your models here.

class Develop(models.Model):
    name = models.CharField('이름', max_length=24)
    developtool = models.ImageField('종류',  max_length=24)
    developdetail = models.CharField('개발툴 설명',max_length =100, default='')
    

    def __str__(self):
        return self.title