from django.urls import path
from Profileapp import views 

urlpatterns = [
    path('',views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('change-password/', views.change_password, name='change_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    # Add the reset_password URL
    path('reset_password/<str:username>/<str:token>/', views.reset_password, name='reset_password'),
]
