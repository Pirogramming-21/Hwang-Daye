from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html',{'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie/movie_detail.html', {'movie': movie})

def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie/movie_edit.html', {'form': form})

def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/movie_edit.html', {'form': form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie_list')