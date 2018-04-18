from django.contrib.auth import views as auth_views
from django.urls import include, path

from .views import *

app_name = 'accounts'

urlpatterns = [
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('password_reset/', auth_views.password_reset,
         {'post_reset_redirect': 'accounts:password_reset_done', },
         name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.password_reset_confirm,
         {'post_reset_redirect': 'accounts:password_reset_complete', },
         name='password_reset_confirm'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name="profile"),
]
