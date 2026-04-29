from django.urls import path
from . import views

urlpatterns = [
    path('',          views.home_view,     name='dashboard_home'),
    path('profile/',  views.profile_view,  name='user_profile'),
    path('settings/', views.settings_view, name='user_settings'),
]
