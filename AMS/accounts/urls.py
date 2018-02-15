from django.urls import include, path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
  path('login/', auth_views.login, name='login'),
  path('logout/', auth_views.logout, name='logout'),
  path('register/', views.register, name='register'),
  path('', include('django.contrib.auth.urls')),
  path('index/', views.index, name='index'),
]
