from django.contrib import admin
from apps_analytics.contacto.models import (
    contactoDepartamento,
    contactoNotificacion,
    contactoPersona,
)
"""
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
import os

def Bakups_ModelsTables(modeladmin, request, queryset):
    ruta = "backup/backups_config/"
    content_type = ContentType.objects.get_for_model(queryset.model, for_concrete_model=False)
    name = content_type.name
    app = content_type.app_label
    schema = content_type.model
    os.system('python manage.py dumpdata '+ app + '.' + schema + ' > ' + ruta  + schema +'.yaml')

admin.site.add_action(Bakups_ModelsTables, "Backups")
"""
admin.site.register(contactoDepartamento)
admin.site.register(contactoNotificacion)
admin.site.register(contactoPersona)

# Register your models here.
