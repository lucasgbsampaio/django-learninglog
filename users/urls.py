"""Define padroes de URL para users"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Pagina de login
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Pagina de logout
    path('logout', views.logout_view, name='logout'),
    # Pagina de cadastro
    path('register', views.register, name='register'),

]