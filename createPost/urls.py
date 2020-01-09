
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'createPost'

urlpatterns = [
    path('', views.create, name="create"),
    path('viewAll/', views.viewAll, name='viewAll'),
    ]



