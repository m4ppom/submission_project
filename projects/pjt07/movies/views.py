from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from .models import Genre, Movie, Review

# Create your views here.
@require_GET
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review_form = ReviewForm()
    reviews = movie.review_set.all()
    is_like = movie.like_users.filter(id=request.user.id).exists()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
        'is_like': is_like,
    })


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {
        'movies': movies,
    })


@login_required
@require_POST
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = ReviewForm(request.POST)
    
    if form.is_valid():
        review = form.save(commit=False)
        review.movie = movie
        review.user = request.user
        review.save()

    return redirect('movies:movie_detail', movie_id)

@require_POST
def delete_review(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id, movie_id=movie_id)
    review.delete()
    return redirect('movies:movie_detail', movie_id)

@require_POST
def like(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)

    if movie.like_users.filter(id=user.id).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)

    return redirect('movies:movie_detail', movie_id)

@login_required
@require_http_methods(['GET', 'POST'])
def update_review(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id, movie_id=movie_id)
    if movie.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance = posting)
            if form.is_valid():
                movie = form.save()
                return redirect('accounts:accounts_detail', user.id)

    
