from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def main(req):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(req, 'posts/list.html', context)

def create(req):
    if req.method == 'POST':
        form = PostForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostForm()
    return render(req, 'posts/post_form.html', {'form': form})
        

def detail(req, pk):
    post = get_object_or_404(Post, pk=pk)
    ctx = {'post': post}
    return render(req, 'posts/detail.html', ctx)

def update(req, pk):
    post = get_object_or_404(Post, pk=pk)
    if req.method == "POST":
        form = PostForm(req.POST, req.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', pk=pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'post': post}
    return render(req, 'posts/update.html', context)

def delete(req, pk):
    post = get_object_or_404(Post, pk=pk)
    if req.method == "POST":
        post.delete()
        return redirect('posts:list')
    context = {'post': post}
    return render(req, 'posts/delete_confirm.html', context)
