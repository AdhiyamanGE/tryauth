from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('',views.regiister,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='appauth/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='appauth/logout.html'), name='logout'),
    path('display/',views.display,name="display"),
    path('status/<str>/',views.statue,name="editval"),
    path('profile',views.profile,name='profile')
]