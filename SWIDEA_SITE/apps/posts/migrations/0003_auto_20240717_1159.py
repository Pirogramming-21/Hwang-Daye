# Generated by Django 3.2.25 on 2024-07-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20240717_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='detail',
            field=models.CharField(default='아이디어 설명', max_length=100, verbose_name='아이디어 설명'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=24, verbose_name='아이디어명'),
        ),
    ]