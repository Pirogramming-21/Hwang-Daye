
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment/', views.comment_ajax, name='comment_ajax'),
    path('delete_comment/', views.delete_comment_ajax, name='delete_comment_ajax'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)