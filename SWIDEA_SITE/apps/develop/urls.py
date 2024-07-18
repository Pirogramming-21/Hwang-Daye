from django.urls import path
from .views import develop_list, develop_register

app_name = 'develop'

urlpatterns = [
    path('list/', develop_list, name='list'),
    path('register/', develop_register, name='register'),
]