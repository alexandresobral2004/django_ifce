from django.contrib import admin
from django.urls import include, path

from . import views


app_name = 'usuario'

urlpatterns = [
    path('novo_usuario/',views.add_user,name='add_user'),
    path('login/',views.UserLogin.as_view(),name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
]