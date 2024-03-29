from django.urls import path, reverse_lazy, include
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='user_profile'),

    path('profile/edit/', edit_profile, name='edit_profile'),
    path('change-password/', change_password, name='change_password'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html',
             success_url=reverse_lazy('accounts:password_reset_done'),
             email_template_name='accounts/emails/pw_reset_email.html', ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete'), ),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html',
    ),
         name='password_reset_complete'),

]
