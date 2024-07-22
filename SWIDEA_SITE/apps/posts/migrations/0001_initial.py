# Generated by Django 3.2.25 on 2024-07-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='제목')),
                ('photo', models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name='이미지')),
                ('content', models.CharField(max_length=24, verbose_name='내용')),
            ],
        ),
    ]