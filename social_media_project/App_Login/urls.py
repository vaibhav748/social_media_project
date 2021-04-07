from django.urls import path, include
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user_other/<username>', views.user, name='user_other'),
    path('follow/<username>', views.follow, name='follow'),
    path('unfollow/<username>', views.unfollow, name='unfollow'),


]