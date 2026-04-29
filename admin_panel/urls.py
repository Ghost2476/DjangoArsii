from django.urls import path
from . import views

urlpatterns = [
    path('',             views.dashboard_view,    name='admin_dashboard'),
    path('users/',       views.users_list_view,   name='admin_users'),
    path('users/<int:pk>/', views.user_detail_view, name='admin_user_detail'),
]
