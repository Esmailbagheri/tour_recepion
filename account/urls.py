from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/<int:user_id>', views.UserProfileView.as_view(), name='user_profile'),
    path('reset/', views.UserPasswordView.as_view(), name='reset_password'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/complete/', views.UserPasswordCompleteView.as_view(), name='password_reset_complete'),
    path('follow/<int:user_id>', views.UserFollowing.as_view(), name='user_follow'),
    path('unfollow/<int:user_id>', views.UserUnfollow.as_view(), name='user_unfollow'),
    path('edit/', views.EditProfileView.as_view(), name='edit_user'),
]