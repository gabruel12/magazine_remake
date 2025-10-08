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
from reserves import views_reserves as vrv

urlpatterns = [
    path('authent/login/', va.login, name="user_login"),
    path('authent/loged/<str:user>/', va.loged,  name="user_loged"),
    path('authent/cadaster/', va.cadaster, name="user_cadaster"),
    path('authent/<str:username_selected>/delete/', va.delete, name="user_delete"),
    path('rooms/create/', vr.create, name="create"),
    path('rooms/<int:room_id>/delete/', vr.delete, name="delete"),
    path('rooms/<str:room_name>/appointments/', vrv.appointments, name="appointments"),
    path('rooms/<str:room_name>/toschedule/', vrv.toschedule, name="schedule"),
    path('rooms/<str:room_name>/filter/', vr.filter, name="filter"),
    path('rooms/<str:schedule_id>/toschedule/delete/', vrv.del_schedule, name="del_schedule")
]
