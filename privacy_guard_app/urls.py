from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('data/', views.data, name='data'),
    path('download_data/', views.download_data, name='download_data'),
    path('delete_data/', views.delete_data, name='delete_data'),
    # Add other app-specific URL patterns here
]

