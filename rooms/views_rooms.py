from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def delete(request, id):
    request.GET.get('id')
    return JsonResponse({'sucess': 'cookie received.'}, status=200)

def filter(request):
    if request.method == "POST":
        
        return JsonResponse({'sucesso': 'requisicao em post'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

def schedule(request):
    if request.method == "POST":
        
        return JsonResponse({'sucesso': 'requisicao em post'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

def create(request):
    if request.method == "POST":
        
        return JsonResponse({'sucesso': 'requisicao em post'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)