from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# 👇 ESTA LÍNEA ES CLAVE
app_name = 'usuarios'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='productos:home'), name='logout'),
]

