import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from authent.models import Users
from logs.models import logger

@csrf_exempt
def cadaster(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    name = data.get('Name')
    username = data.get('Username')
    username = username.lower()
    email = data.get('Email')
    password = data.get('Password')

    if not all([username, name, email, password]):
        return JsonResponse({'error': 'Missing fields'})

    if Users.objects.filter(username=username).exists():
        return JsonResponse({'error': 'This username already exists'}, status=400)
    
    user = Users(username=username, name=name, email=email, password=password)
    user.save()
    logger("success_user_create", thing=user)
    return JsonResponse({'success': 'The user was create'}, status=201)
    
@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    username_selected = data.get('Username')
    your_password = data.get('Password')
    
    if Users.objects.filter(username=username_selected).exists():
        if Users.objects.filter(password=your_password):
            logger("success_user_login", thing=username_selected)
            return JsonResponse({'success': 'Welcome back!'})
        else:
            return JsonResponse({'error': 'Incorrect password.'}, status=400)
    else:
        return JsonResponse({'error': 'User not exists'}, status=400)

@csrf_exempt
def delete(request, username_selected):
    if request.method != "GET":
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    username_selected = request.GET.get('username')
    if Users.objects.filter(username=username_selected).exists():
        user_obj = Users.objects.get(username=username_selected)
        user_obj.delete()
        return JsonResponse({'success': 'deleted account!'}, status=200)
    else:
        return JsonResponse({'error': 'User not exists'}, status=400)