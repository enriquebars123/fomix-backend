from rest_framework.response import Response
from rest_framework import status
from apps_user.smxAnalitica_user.models import user
from smx_analytics.libraryBusiness.libUtility import utility
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
#import secrets
import uuid
import os

class PasswordReset(APIView):
        
    def post(self, request, *args, **kwargs):
        try:
            #print("aki sige server")
            #print(os.environ.get('serverFrontend'))
            if os.environ.get('serverFrontend') == None:
                serverFrontend = config('serverFrontend')
            else:
                serverFrontend = os.environ.get('serverFrontend')
            data = request.data
            to = []
            User = user.objects.get(email = data.get('email'))
            if User.activo :  
                #token = secrets.token_hex()
                uid = str(uuid.uuid4())
                url = serverFrontend + uid
                #print(url)

                contenido = str(config('contenido_Recuperacion')).format(url, url)
                to.append(User.email)
                result = utility.Gmail(self, config('asunto_Recuperacion'), to ,contenido )
                User.token = uid
                User.save()
                if result["success"] == True:
                    return Response(result, status.HTTP_200_OK)
                else :
                    return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            else :
                result = { "success": False, "msg": "Error - Usuario desactivado temporalmente - notificar a TI" }
                return Response(result, status.HTTP_401_UNAUTHORIZED)

        except user.DoesNotExist: 
            result ={ "success": False , "msg" : "Error - Correo no existe..."}
            return Response(result, status.HTTP_401_UNAUTHORIZED)


class PasswordResetDone(APIView):
    def post(self, request, *args, **kwargs):
        try:
            result = {"success": True, "msg" : "registro actualizado correctamente..."}
            data = request.data
            #print(data)
            User = user.objects.get(token=data.get("token"))
            User.set_password(data.get("password"))
            User.token = ""
            User.save()
            return Response(result, status.HTTP_200_OK)
        except user.DoesNotExist:
            result = {"success": False, "msg": "Error - No existe token"}    
        return Response(result,status.HTTP_401_UNAUTHORIZED)



