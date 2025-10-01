from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rooms.models import Room
from reserves.models import Schedules

@csrf_exempt
def toschedule(request, user):
    if request.method != "GET":

@csrf_exempt
def appointments(request, room_name):
    if request.method != "GET":
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    if Room.objects.filter(name=room_name).exists():
        return JsonResponse({'success': f'This is appointments who {room_name} have!'}, status=200)
    else:
        return JsonResponse({'error': 'This room does not exists'}, status=400)  # <-- mostrar agendamentos depois 