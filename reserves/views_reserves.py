import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rooms.models import Room
from reserves.models import Schedules
from authent.models import Users
from reserves.utils import get_session_user, make_reserve
from django.core.exceptions import ObjectDoesNotExist
from logs.models import logger

@csrf_exempt
def toschedule(request, room_name):
    user = get_session_user(request)
    if not user:
        return JsonResponse({'error': 'You are not logged in'}, status=401)

    try:
        room = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)

    logger("success_schedule_create", thing=room, none=user)
    return make_reserve(request, room, user)

@csrf_exempt
def appointments(request, room_name):
    if request.method != "GET":
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        room = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        return JsonResponse({'error': 'This room does not exists'}, status=404)
    
    room_appointments = Schedules.objects.filter(room_reserved=room)

    appointment_list = []
    for appt in room_appointments:
        appointment_list.append({
        "created_by": appt.created_by.username if appt.created_by else None,
        "start_time": appt.start_time.strftime("%d/%m/%Y %H:%M"),      ## <-- fazer com que esse modelo de hora seja pra todos
        "end_time": appt.end_time.strftime("%d/%m/%Y %H:%M")
    })
    
    return JsonResponse({
        'success': f'This is appointments who the room "{room_name}" have!',
        'appointments': appointment_list,
        'Info': 'If you want delete some schedule, please get your schedule id'
    }, status=200)

def del_schedule(request, schedule_id):
    user = get_session_user(request)
    if not user:
        return JsonResponse({'error': 'You are not logged in'}, status=401)

    if request.method != "GET":
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        room_obj = Schedules.objects.get(id=schedule_id)
        room_obj.delete()

        logger("success_schedule_delete", thing=schedule_id, none=user)
        return JsonResponse({'success': 'This room has been deleted successfully!'}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'This schedule does not exists'}, status=400)

    except Exception as e:
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
