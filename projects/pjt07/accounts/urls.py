from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.accounts_list, name='accounts_list'),
    path('<int:user_id>/', views.accounts_detail, name='accounts_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]