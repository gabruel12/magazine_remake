from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rooms.models import Room

@csrf_exempt
def create(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

    try:
         data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)

    room_name = data.get('room_name')
    room_capacity = data.get('room_capacity')
            
    if not all([room_capacity, room_name]):
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)
            
    create_room = Room(name=room_name, capacity=room_capacity)
    create_room.full_clean()
    create_room.save()

    return JsonResponse({'success': 'The room was create.'}, status=201)

def filter(request, room_name):
    if request.method != "GET":
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    if Room.objects.filter(name=room_name).exists():
        room_obj = Room.objects.get(name=room_name)
        room_obj = {
            'id': room_obj.id,
            'name': room_obj.name,
            'capacity': room_obj.capacity 
        }
        return JsonResponse({'success': room_obj}, status=200)
    else:
        return JsonResponse({'error': 'No rooms found.'}, status=400)

def delete(request, room_id):
    if request.method != "GET":
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    if Room.objects.filter(id=room_id).exists(): 
        room_obj = Room.objects.get(id=room_id)
        room_obj.delete()

        return JsonResponse({'success:': 'The room is deleted.'})
    else:
        return JsonResponse({'error': 'This room not exists.'}, status=400)