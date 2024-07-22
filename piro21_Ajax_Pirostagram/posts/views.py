from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('posts:post_detail', pk=post.pk)  # 'posts:post_detail'로 리디렉션
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
import json


@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']

    post = Post.objects.get(id=post_id)

    if button_type =='like':
        post.like += 1
    else:
        post.dislike += 1

    post.save()

    return JsonResponse({'id': post_id, 'type': button_type})

@csrf_exempt
def comment_ajax(request):
    req = json.loads(request.body)
    post_id = req['post_id']
    content = req['content']

    post = Post.objects.get(id=post_id)
    comment = Comment.objects.create(post=post, content = content)

    return JsonResponse({'post_id':post_id, 'content':content, 'created_at':comment.created_at})

@csrf_exempt
def delete_comment_ajax(request):
    if request.method == 'DELETE':
        req = json.loads(request.body)
        comment_id = req['comment_id']

        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({'comment_id': comment_id})
        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment does not exist'}, status=404)
    else:
        return HttpResponseNotAllowed(['DELETE'])