from rooms.models import Room
from reserves.models import Schedules
from authent.models import Users
import json
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from django.db.models import Q

## ENCAPSULATION FUNCTIONS

def get_session_user(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    try:
        return Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        return None

def make_reserve(request, room: Room, user: Users):
    if request.method == "GET":
        return JsonResponse({'Info': 'Please change to POST to pass others informations'})

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        start = data.get('Start-time')
        end = data.get('End-time')

        if not all([start, end]):
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        start_dt = parse_datetime(start)
        end_dt = parse_datetime(end)

        if not start_dt or not end_dt:
            return JsonResponse({'error': 'Invalid datetime format'}, status=400)
        if not start_dt <= end_dt:
            return JsonResponse({'error': 'Start time must be before end time'}, status=400)

        conflict = Schedules.objects.filter(
            room_reserved=room,
            start_time__lt=end_dt,
            end_time__gt=start_dt
        ).exists()
        if conflict:
            return JsonResponse({'error': 'Just have a reserve in this hour'}, status=400) # <-- No front já não vai dar opção de
#                                                                                             agendar um horário já escolhido não é?
        try:
            create_schedule = Schedules(
                created_by=user,
                room_reserved=room,
                start_time=start,
                end_time=end
                )
            create_schedule.save()

            return JsonResponse({
                'success': 'Success to create room reserve',
                'id': create_schedule.id
            })
        except Exception as e:
            return JsonResponse({'error': f'Error to make reserve: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

