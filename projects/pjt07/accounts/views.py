from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth import login as auth_login, logout as auth_log_out
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import get_user_model
from .models import User
from movies.forms import ReviewForm


User = get_user_model()

# @require_GET
# def user_page(request, user_id):
#     user_info = get_object_or_404(User, id=user_id)
#     return render(request, 'accounts/user_page.html', {
#         'user_info': user_info,
#     })


def logout(request):
    auth_log_out(request)
    return redirect('movies:movie_list')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:movie_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:movie_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def accounts_list(request):
    users = User.objects.all()
    return render(request, 'accounts/accounts_list.html', {
        'users': users,
    })


def accounts_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    reviews = user.review_set.all().order_by('id')
    like_movies = user.like_movies.all()
    # if request.user == user:
    #     form = ReviewForm(request, instance=review)
    # review_form = ReviewForm()
    return render(request, 'accounts/accounts_detail.html', {
        'user': user,
        'reviews': reviews,
        'like_movies': like_movies,
        # 'form': form,
        # 'review_form': review_form,
    })

