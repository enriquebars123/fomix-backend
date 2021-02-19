# Django rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

# modelos
from apps_analytics.referencias.models import *
from apps_analytics.catalogo.models import *
from apps_analytics.relacion.models import * 
from apps_analytics.referencias.models import * 
from apps_analytics.metodo.models import * 


# serializers
from apps_analytics.catalogo.api.serializers import *
from apps_analytics.relacion.api.serializers import *
from apps_analytics.referencias.api.serializers import *
from apps_analytics.metodo.api.serializers import *


#relacionCompPredictivo
class ListPredictivo(APIView):
    def get(self, request):
        result = []
        
        #d = [CompPredictivoSerializers(predictivos).data for  predictivos in relacionCompPredictivo.objects.all()]
        objPredic = relacionCompPredictivo.objects.all()
        for comPredic in objPredic : 
            print(comPredic.id)
            seriComponete = ComponenteSerializers(comPredic.componentes)
            seriMaquina = RefMaquinaPredSerializers(comPredic.maquina)
            seriPredictivo = PredictivoSerializers(comPredic.predictivo)
            ListFuenteDato = []
            idMaquina = seriMaquina.data['id']
            objFuenteDatos = relacionPredFuenteDatos.objects.filter(predictivo=comPredic.predictivo.id)
            
            #obtengo las referencias
            seriLinea = RefLineaSerializers(comPredic.maquina.linea)
            seriPlanta = RefPlantaSerializers(comPredic.maquina.linea.planta)
            seriEmpresa = RefEmpresaSerializers(comPredic.maquina.linea.planta.empresa)

            for fuenteDato in objFuenteDatos :
                seriFuenteDatos  = FuenteDatosSerializers(fuenteDato.fuenteDatos).data
                objRefMaqFuenteDatos = []
                try:
                    objRefMaqFuenteDatos = relacionMaqFuenteDatos.objects.get(maquina=idMaquina,fuenteDatos=fuenteDato.fuenteDatos.id)
                    seriFuenteDatos['maquinaExternaId'] = MaqFuenteDatoSerializers(objRefMaqFuenteDatos).data['referenciaId']
                except :
                    seriFuenteDatos['maquinaExternaId'] = []
                ListFuenteDato.append(seriFuenteDatos)
                #ListFuenteDato.append(FuenteDatosSerializers(fuenteDato.fuenteDatos).data)
            metodo_procesamiento = []
            metodoProc = metodoProcesamiento.objects.filter(predictivo=comPredic.predictivo.id)


            print(metodoProc)
            for objProc in metodoProc:
                print(objProc)
                listParams = metodoProcSerializers(objProc).data
                seriMetodoProc = metodoProcSerializers(objProc).data
                seriMetodoProc["catalogoProc"] = metodoCatalogoProcSerializers(objProc.catalogoProc).data
                metodo_procesamiento.append(seriMetodoProc)
            
            referencia = {
                "maquina": seriMaquina.data,
                "linea": seriLinea.data,    
                "planta": seriPlanta.data,
                "empresa": seriEmpresa.data,
            }

            data = {
                "id": comPredic.id,
                "predictivo" : seriPredictivo.data,
                "componentes": seriComponete.data,
                "referencias": referencia,
                "fuenteDatos": ListFuenteDato,
                "metodo_procesamiento": metodo_procesamiento
            
            }       
            result.append(data)
        return Response(result , status.HTTP_200_OK)


class getPredictivoDetails(APIView):

    def get_object(self, pk):
        try:
            return relacionCompPredictivo.objects.get(id=pk)
        except relacionCompPredictivo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objPredic = []
        instance = self.get_object(pk)
        result = []
        seriComponete = ComponenteSerializers(instance.componentes)
        seriMaquina = RefMaquinaPredSerializers(instance.maquina)
        seriPredictivo = PredictivoSerializers(instance.predictivo)
        ListFuenteDato = []
        idMaquina = seriMaquina.data['id']
        objFuenteDatos = relacionPredFuenteDatos.objects.filter(predictivo=instance.predictivo.id)
        
        #obtengo las referencias
        seriLinea = RefLineaSerializers(instance.maquina.linea)
        seriPlanta = RefPlantaSerializers(instance.maquina.linea.planta)
        seriEmpresa = RefEmpresaSerializers(instance.maquina.linea.planta.empresa)

        for fuenteDato in objFuenteDatos :
            seriFuenteDatos  = FuenteDatosSerializers(fuenteDato.fuenteDatos).data
            objRefMaqFuenteDatos = []
            try:
                objRefMaqFuenteDatos = relacionMaqFuenteDatos.objects.get(maquina=idMaquina,fuenteDatos=fuenteDato.fuenteDatos.id)
                seriFuenteDatos['maquinaExternaId'] = MaqFuenteDatoSerializers(objRefMaqFuenteDatos).data['referenciaId']
            except :
                seriFuenteDatos['maquinaExternaId'] = []
            ListFuenteDato.append(seriFuenteDatos)
            #ListFuenteDato.append(FuenteDatosSerializers(fuenteDato.fuenteDatos).data)
        
        metodo_procesamiento = []
        metodoProc = metodoProcesamiento.objects.filter(predictivo=instance.predictivo.id)
        
        for objProc in metodoProc:
            params = []
            listParams = metodoProcSerializers(objProc).data
            #print(objProc)
            seriMetodoProc = metodoProcSerializers(objProc).data
            seriMetodoProc["catalogoProc"] = metodoCatalogoProcSerializers(objProc.catalogoProc).data
            metodo_procesamiento.append(seriMetodoProc)
        
        referencia = {
            "maquina": seriMaquina.data,
            "linea": seriLinea.data,    
            "planta": seriPlanta.data,
            "empresa": seriEmpresa.data,
        }

        data = {
            "id": instance.id,
            "predictivo" : seriPredictivo.data,
            "componentes": seriComponete.data,
            "referencias": referencia,
            "fuenteDatos": ListFuenteDato,
            "metodo_procesamiento": metodo_procesamiento
        }       
        result.append(data)
        return Response(result , status.HTTP_200_OK)
