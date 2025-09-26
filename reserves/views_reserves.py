from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rooms.models import Room
from reserves.models import Schedules

@csrf_exempt
def schedules(request):
    room_name = method.GET.get('room')
    room = get_object_or_404(Room, name=room_name)

    if request.method == "POST":
        room_name_db = request.POST.get('Room_Name')
        date = reqeust.POST.get('Schedule_Date')
        
    