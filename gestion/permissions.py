from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from django.contrib.auth.models import AnonymousUser


class SoloAdmin(BasePermission):

#si queremos cambiar el mensaje  de resuesta cuando falle la validacion
#  
    message = 'tu no tienes los permisios necesarios'
    
    def has_permission(self, request, view):

        print(SAFE_METHODS)
        if request.method in SAFE_METHODS:
            return True

        if  isinstance(request.user , AnonymousUser):
            return False

        if request.user.tipoUsuario  == 'ADMIN':
            return  True
        else:
            return False