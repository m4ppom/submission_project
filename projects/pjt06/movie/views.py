from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Comment
from .forms import MovieModelForm, CommentModelForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {
        'movies': movies,
    })


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    comments = movie.comment_set.all().order_by('id')
    comment_form = CommentModelForm()
    return render(request, 'movie/movie_detail.html', {
        'movie': movie,
        'comments': comments,
        'comment_form': comment_form,
    })


@require_http_methods(['GET', 'POST'])
def new_movie(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie:movie_list')
    else:
        form = MovieModelForm()
    return render(request, 'movie/new_movie.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect(movie)
    else:
        form = MovieModelForm(instance=movie)
    return render(request, 'movie/update_movie.html', {
        'form': form,
    })


@require_POST
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movie:movie_list')


@require_POST
def new_comment(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie_id = movie.id
        comment.save()
    return redirect(movie)


@require_POST
def delete_comment(request, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, movie_id=movie_id)
    comment.delete()
    return redirect(comment.movie)
