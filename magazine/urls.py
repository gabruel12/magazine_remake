"""
URL configuration for magazine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authent import views_authent as va
from rooms import views_rooms as vr

urlpatterns = [
    path('authent/login/', va.login, name="login"),
    path('authent/cadaster/', va.cadaster, name="cadaster"),
    path('rooms/create/', vr.create, name="create"),
    path('rooms/<str:id>/delete/', vr.delete, name="delete"),
    path('rooms/<str:name>/schedule/', vr.schedule, name="schedule"),
    path('rooms/<str:name>/filter', vr.filter, name="filter"),
]
