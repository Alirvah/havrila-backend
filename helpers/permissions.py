from rest_framework import permissions
from django.conf import settings

class FastTokenAllow(permissions.BasePermission):

    message = 'Only FAST TOKEN can access APIs'

    def has_permission(self, request, view):
        try:
            token = request.query_params['t']
        except Exception as e:
            self.message = "Permission denied wrong TOKEN"
            return False
        return token == settings.FAST_TOKEN