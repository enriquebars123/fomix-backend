import os, sys
from django.conf import settings
from django.core.mail import (
    EmailMultiAlternatives, 
    EmailMessage
)
from rest_framework.response import Response
from rest_framework import status
from decouple import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


"""
    libreria de utilidad, usala para crear metodos reutilizables,

"""


class utility():

    def search_file(self, path, ext):
        lstFiles = []
        lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ext):
                    lstFiles.append(nombreFichero) 
        #print ('LISTADO FINALIZADO')
        return lstFiles
    
    
    def Gmail(self, asunto, destinatario, contenido):
        try:
            print(asunto)
            print(settings.EMAIL_HOST_USER)
            print(destinatario)
            result = {"success": True, "msg": "Email enviado..."}
            subject, from_email, to = asunto , settings.EMAIL_HOST_USER , destinatario
            text_content = 'FOMIX WEB.'
            html_content = contenido
          
            

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return result
           
        except smtplib.SMTPException as e:
            result = {"success" : False , "msg": 'Error - SMTPException: %s' % str(e)}
            
        return result
    

    def get_server(self, url, path):
        return  url.replace(path,'')  
