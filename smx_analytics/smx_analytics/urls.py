from django.contrib           import admin
from django.urls              import path
from django.conf.urls.static  import static
from django.conf.urls         import url, include 
from django.conf              import settings
from rest_framework           import routers

"""

    DEVELOPER BACKEND : JOSE ENRIQUE BECERRA PALACIOS (enriquebars)
    CONSULTORIA : CONSISS
    EMAIL : enriquebars123@gmail.com.mx

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from apps_user.smxAnalitica_user.api.user.views import Login
from apps_analytics.relacion.api.refPerfilMenu.views import *
from apps_analytics.relacion.api.refUserPerfil.views import *
from apps_analytics.relacion.api.refCompPredictivoResult.views import *
from apps_analytics.referencias.api.views import *
from apps_analytics.catalogo.api.views import *
from apps_analytics.relacion.api.views import *
from apps_user.smxAnalitica_user.api.views import *
from apps_analytics.variables.api.views import *
from apps_analytics.regla.api.views import *
from apps_analytics.metodo.api.views import *
from apps_analytics.contacto.api.views import *
from apps_analytics.catalogo.api.catalogoPredictivo.views import *
from apps_celery.procesamiento.views import preProcesamiento
from apps_analytics.metodo.api.metodoProcesamiento.views import *
from apps_analytics.relacion.api.refPredFuenteDatos.views import *
from apps_user.smxAnalitica_user.api.userPasswordReset.views import *
from apps_user.smxAnalitica_user.api.user import views
from apps_analytics.relacion.api.refMaqFuenteDatos.views import *   
# LISTADO DE LAS APIS.


router = routers.DefaultRouter()
router.register('api/v1/refEmpresa'  ,refEmpresaViewSet)
router.register('api/v1/refPlanta'   ,refPlantaViewSet)
router.register('api/v1/refLinea'    ,refLineaViewSet)
router.register('api/v1/refMaquina'  ,refMaquinaViewSet)
router.register('api/v1/perfil', perfilViewSet)
router.register('api/v1/menu', menuViewSet)
router.register('api/v1/fuenteDatos', fuenteDatosViewSet)
router.register('api/v1/predictivo', predictivoViewSet)
router.register('api/v1/componente', componenteViewSet)
router.register('api/v1/perfilMenu', PerfilMenuViewSet)
router.register('api/v1/userPerfil', UserPerfilViewSet)
router.register('api/v1/comPredictivo', CompPredictivoViewSet)
router.register('api/v1/predFuenteDatos', PredFuenteDatosViewSet)
router.register('api/v1/user', UserViewSet)
router.register('api/v1/userArea', UserAreaViewSet)
router.register('api/v1/variables', VariablesViewSet)
router.register('api/v1/reglaComponentes', reglaViewSet)
router.register('api/v1/metodoCatalogo', metodoCatalogoViewSet)
router.register('api/v1/metodoCatalogoProc', metodoCatalogoProcViewSet)
router.register('api/v1/metodoProc', metodoProcViewSet)
router.register('api/v1/catalogoVarDependiente', VariableViewSet)
router.register('api/v1/simbologia', simbologiaViewSet)
router.register('api/v1/regla', reglaViewSet)
router.register('api/v1/contactoNotificacion', contactoNotificacionViewSet)
router.register('api/v1/contactoDepartamento', contactoDepartamentoViewSet)
router.register('api/v1/contactoPersona', contactoPersonaViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    url('', include(('apps_user.smxAnalitica_user.api.urls', 'Api_smxAnalitica_user'), namespace='Api_smxAnalitica_user')),
    url('', include(('apps_analytics.referencias.api.urls', 'Api_referencia'), namespace='Api_referencia')),
    url('', include(('apps_analytics.catalogo.api.urls', 'Api_catalogo'), namespace='Api_catalogo')),
    url('', include(('apps_analytics.relacion.api.urls', 'Api_relacion'), namespace='Api_relacion')),
    url('', include(('apps_analytics.variables.api.urls', 'Api_variables'), namespace='Api_variables')),
    url('', include(('apps_analytics.metodo.api.urls', 'Api_metodo'), namespace='Api_metodo')),
    url('', include(('apps_analytics.regla.api.urls', 'Api_regla'), namespace='Api_regla')),
    url('', include(('apps_analytics.contacto.api.urls', 'Api_contacto'), namespace='Api_contacto')),
   
    # -------------------------------------
    ## APIS FUERA DE MODELS 
    # -------------------------------------
    # Iniciar session
    url(r'^api/v1/sesion', Login.as_view()),
    
    # -------------------------------------
    ## API REPORTE PREDICTIVO Y REALES 
    # -------------------------------------
    url(r'^api/v1/predictivosItems/$', predictivosItems.as_view(), name="url"),
    url(r'^api/v1/reporteRealPredictivo/$', reporteRealPredictivo.as_view(), name="url"),
    url(r'^api/v1/predictivoDMC/$', predictivoDMC.as_view(), name="url"),
    url(r'^api/v1/reporteIndependiente/$', reporteIndependiente.as_view(), name="url"),
    url(r'^api/v1/QDADmc/$', QDADmc.as_view(), name="url"),
    # OBTENCION DE VARIABLES INDEPENDINETES Y DEPENDIENTES
    path('api/v1/variablesIndependientes/<int:pk>/', variablesIndependientes.as_view()),
    path('api/v1/variablesDependientes/<int:pk>/', variablesDependientes.as_view()),
    # Obtiene todos los predictivos y informacion detallada.
    #url(r'^api/v1/PasswordReset/(?P<hash>\w+)/$', PasswordReset.as_view(), name="url"),
    path('api/v1/getPredictivoDetails/<int:pk>/', getPredictivoDetails.as_view()),
    url(r'^api/v1/bulkPerfilMenu', bulkPerfilMenu.as_view()),
    url(r'^api/v1/DeletePerfilMenu', DeletePerfilMenu.as_view()),
    url(r'^api/v1/bulkUserPerfil', bulkUserPerfil.as_view()),
    url(r'^api/v1/DeleteUserPerfil', DeleteUserPerfil.as_view()),   
    url(r'^api/v1/ListPredictivo', ListPredictivo.as_view()),   
    url(r'^api/v1/DeleteMetodProc', DeleteMetodProc.as_view()),
    url(r'^api/v1/DeletePredFueteDatos', DeletePredFueteDatos.as_view()),
    url(r'^api/v1/DeleteMaqFuenteDatos', DeleteMaqFuenteDatos.as_view()),
    url(r'^api/v1/bulkMaqFuenteDatos',bulkMaqFuenteDatos.as_view()),
    url(r'^api/v1/preProcesamiento', preProcesamiento.as_view()),
    
    # valida reseteo password por correo 
    url(r'^api/v1/PasswordReset/', PasswordReset.as_view(), name="url"),
    # resetea la password 
    url(r'^api/v1/PasswordResetDone/', PasswordResetDone.as_view(), name="url"),
    # activa cuenta por correo.
    url(r'^ActivateAccount/(?P<hash>\S+)/$', views.ActivateAccount, name="url"),
    url(r'^redirect/', views.redirectLogin, name="url"),
   
   
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

#static(settings.STATIC_URL)
