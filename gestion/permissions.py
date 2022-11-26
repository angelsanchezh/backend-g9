from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class SoloAdmin(BasePermission):

#si queremos cambiar el mensaje  de resuesta cuando falle la validacion
#  
    message = 'tu no tienes los permisios necesarios'
    
    def has_permission(self, request, view):

        print(SAFE_METHODS)
        if request.method in SAFE_METHODS:
            return True

        print(request.user)
        print(view)
        if request.user.tipoUsuario  == 'ADMIN':
            return  True
        else:
            return False