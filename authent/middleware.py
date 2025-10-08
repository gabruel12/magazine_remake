from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from .models import Users

class CustomAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = Users.objects.get(id=user_id)
                request.user = user
            except Users.DoesNotExist:
                request.exist = AnonymousUser()
        else:
            request.user = AnonymousUser()