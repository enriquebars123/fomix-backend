"""Views de ralacion """


# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apps_analytics.regla.models import regla
from rest_framework import status
import json
from decouple import config
from smx_analytics.libraryBusiness.libUtility import utility

# serializer
from apps_analytics.regla.api.serializers import reglaSerializers
from apps_analytics.contacto.models import (
    contactoNotificacion,
    contactoPersona,
)
from apps_analytics.relacion.api.serializers import (
    PerfilMenuSerializers,
    UserPerfilSerializers,
    CompPredictivoSerializers,
    PredFuenteDatosSerializers,
    MaqFuenteDatoSerializers,
    CompPredictivoResultSerializers
)
from apps_analytics.catalogo.api.serializers import (
    VariableSerializers,
)

from apps_analytics.catalogo.models import (
    catalogoVariable,
)

from apps_analytics.referencias.models import referenciaMaquina
# Models
from apps_analytics.relacion.models import (
    relacionPerfilMenu,
    relacionUserPerfil,
    relacionCompPredictivo,
    relacionPredFuenteDatos,
    relacionMaqFuenteDatos,
    relacionCompPredictivoResult,
)

# Utilerias
from smx_analytics.utilerias import GeneralViewSetMixin


class PerfilMenuViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['perfil','menu',]
    filter_backends = [DjangoFilterBackend,]
    queryset = relacionPerfilMenu.objects.all()
    serializer_class = PerfilMenuSerializers
    


class UserPerfilViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['user','perfil',]
    filter_backends = [DjangoFilterBackend,]
    queryset = relacionUserPerfil.objects.all()
    serializer_class = UserPerfilSerializers


class CompPredictivoViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = [ 'componentes','predictivo',]
    filter_backends = [DjangoFilterBackend,]
    queryset = relacionCompPredictivo.objects.all()
    serializer_class = CompPredictivoSerializers


class PredFuenteDatosViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['fuenteDatos','predictivo',]
    filter_backends = [DjangoFilterBackend,]
    queryset = relacionPredFuenteDatos.objects.all()
    serializer_class = PredFuenteDatosSerializers
    """
    create() : para poder agregar una fuente de datos debe de estar dado de alta antes el idReferencia Maquina externa 
    relacion_MaqFuenteDatos.
    """
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            predFuenteDatos = request.data.copy()
            #print(data.get('maquina'))
            idMaq = referenciaMaquina.objects.get(id=data.get('maquina'))

            
            instanceRefMaqFuenteDatos = relacionMaqFuenteDatos.objects.filter(maquina=idMaq, fuenteDatos= data.get('fuenteDatos'))
            if instanceRefMaqFuenteDatos.count():
                del predFuenteDatos['maquina']
                serializer = self.get_serializer(data = predFuenteDatos)
                if serializer.is_valid():
                    obj = serializer.save()
                result = {
                    'success': True,
                    'msg': 'Registro Creado',
                    'data': serializer.data,
                }
                return Response(result, status.HTTP_201_CREATED)
            else :
                result = {"success": False, "msg": "No existe referencia Maquina - Fuente de datos"}
                return Response(result, status.HTTP_400_BAD_REQUEST)
        except referenciaMaquina.DoesNotExist :
            result = {"success": False, "msg": "No existe referencia Maquina - Fuente de datos"}
            return Response(result, status.HTTP_400_BAD_REQUEST)

    
class MaqFuenteDatosViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['maquina','fuenteDatos',]
    filter_backends = [DjangoFilterBackend,]
    queryset = relacionMaqFuenteDatos.objects.all()
    serializer_class = MaqFuenteDatoSerializers


class CompPredictivoResultViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = relacionCompPredictivoResult.objects.all()
    serializer_class = CompPredictivoResultSerializers


    def get_escalamiento(self,obj):
        #print("entre get_escalamiento")
        #objVarDependiente = catalogoVariable.
        listVarError = []
        #listVar = json.loads(obj['jsonPrediccion'])
        listVar = obj['jsonPrediccion']
        #print(listVar)
        for item in listVar:
            #print(item['id'])
            try:             
                itemVar = regla.objects.get(variable=int(item['id']))
                nomVar = itemVar.variable.nombre
                if not (item['result'] >= itemVar.lsl and item['result'] <= itemVar.usl) :
                    objVar = reglaSerializers(itemVar).data
                    objVar['nominal'] = item['result']
                    objVar['variable'] = nomVar
                    del objVar['estatus']
                    del objVar['id']
                    listVarError.append(objVar)
            except regla.DoesNotExist:
                print("NO EXISTE REGLA..")
        #print(listVarError)
        return listVarError
        #return "test"

    def correoNotificar(self, predictivo):

        notificar = contactoNotificacion.objects.get(tipoEjecucion = 1)
        #print(notificar.nombre)
        #print(notificar.tipoEjecucion)
        asunto = str(config('asunto_fallas')).format(notificar.nombre)
        contenidoTRTH = ("""<tr><td width=\"260\" valign=\"top\"><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"><tr bgcolor=\"#eeeeee\" style=\"color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 10px; box-shadow: 0px 0px 0px 2px #666666; border-radius: 1px;\"> """ +
	    """<td style=\"padding-left:5px;\"><h4>Variable</h4></td><td style=\"padding-left:5px;\"><h4>Nominal</h4></td><td style=\"padding-left:5px;\"><h4>USL</h4></td><td style=\"padding-left:5px;\"><h4>LSL</h4></td>""" +
        """<td style=\"padding-left:5px;\"><h4>UCL</h4></td><td style=\"padding-left:5px;\"><h4>LCL</h4></td></tr>""")
        contenidoTRTD = "<tr style=\"color: #153643; font-family: \'open sans\', \'helvetica neue\', helvetica, arial, sans-serif; line-height: 30px;\"><td style=\"padding: 5px 0 0 5px;\"> {} </td><td style=\"padding: 5px 0 0 5px;\"> {} </td><td style=\"padding: 5px 0 0 5px;\"> {} </td><td style=\"padding: 5px 0 0 5px;\"> {} </td><td style=\"padding: 5px 0 0 5px;\"> {} </td><td style=\"padding: 5px 0 0 5px;\"> {} </td></tr>"
        #print(contenidoTRTH)
        contenidoTable = ("""<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"><tr><td style=\"padding: 10px 0 30px 0;\"><table align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"600\" style=\"border: 1px solid #cccccc; border-collapse: collapse;\">""" +
		"""<tr><td align=\"center\" bgcolor=\"#eeeeee\" style=\"padding: 40px 0 30px 0; color: #153643; font-size: 28px; font-weight: bold; font-family: Arial, sans-serif;\"><img src=\"./sisamex.png\" alt=\"Creating Email Magic\" height=\"50\" />""" +
		"""</td></tr><tr><td bgcolor=\"#ffffff\" style=\"padding: 40px 30px 40px 30px;\"><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"><tr><td style=\"color: #153643; font-family: Arial, sans-serif; font-size: 24px;\">"""	+
		"""<b>Seguimiento a fallas de variables</b></td></tr><tr><td style=\"padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit."""	+ 
		"""In tempus adipiscing felis, sit amet blandit ipsum volutpat sed. Morbi porttitor, eget accumsan dictum, nisi libero ultricies ipsum, in posuere mauris neque at erat.</td></tr><tr><td><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\">"""	+
		"""<tr><td width=\"260\" valign=\"top\"><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"> {} {} </table></td></tr></table></td></tr></table></td></tr><tr><td bgcolor=\"#ee4c50\" style=\"padding: 30px 30px 30px 30px;\">"""	+
		"""<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"><tr><td style=\"color: #ffffff; font-family: Arial, sans-serif; font-size: 11px;\" width=\"75%\">&reg; Sisamex 2020<br/><br/>Has recibido este correo porque te has suscrito al sistema de alertas del Sistema de Analítica<br/>""" 	+
		"""Si deseas cancelar tu suscripción todas las alertas de correo haz click <a href=\"#\" style=\"color: #ffffff;\"><font color=\"#ffffff\">aquí</font></a></td></tr></table></td></tr></table></td></tr></table>""")
        countcontenidoTRTD = ""              
        for item in predictivo["listError"]:
            #print(item["variable"])
            TRTD = str(contenidoTRTD).format(item["variable"], item["nominal"], item["usl"], item["lsl"], item["ucl"], item["lcl"])
            countcontenidoTRTD += TRTD
        
        contenido = str(contenidoTable).format(contenidoTRTH,countcontenidoTRTD)
        correosCatalogo = contactoPersona.objects.filter(departamento_id__in=notificar.departamento.all().values('id'))
        #print(correosCatalogo)
        #itemdes = ""
        listCorreos = []
        for item in correosCatalogo:
            listCorreos.append(item.correo)
        #print(listCorreos)
            #destinos = itemdes[:-1]
        
        result = utility.Gmail(self, asunto, listCorreos ,contenido )
        #print(result)

    def create(self, request, *args, **kwargs):
        predictivoInfo = request.data
        serializer = self.get_serializer(data=request.data)
        #print(serializer)
        if serializer.is_valid():
            obj = serializer.save()
            serializer = self.get_serializer(obj)
            #r["id"] = obj.id
            mhttp_status = status.HTTP_201_CREATED
            
            listVariable = self.get_escalamiento(predictivoInfo)
            #print(len(listVariable))
            if len(listVariable):
                result = {
                    "numSerie": predictivoInfo['codigoPieza'],
                    "fecha": predictivoInfo['fecha'],
                    "listError" : listVariable
                }
                self.correoNotificar(result)
            respuesta = {
                'success': True,
                'msg': 'Registro Creado',
                'data' : serializer.data
            }
        else:
            mhttp_status = status.HTTP_400_BAD_REQUEST
            respuesta = {
                'success': False,
                'msg': '%s' % serializer.errors,
                'result' : []
            }
       
            
        #if serializer.is_valid():
            #print(serializer)

        return Response(respuesta, status.HTTP_201_CREATED)
