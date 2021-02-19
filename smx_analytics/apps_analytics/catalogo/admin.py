from django.contrib import admin
from apps_analytics.catalogo.models import (
    catalogoMenu,
    catalogoComponente,
    catalogoFuenteDatos,
    catalogoPerfil,
    catalogoPredictivo,
)

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
import os
from decouple import config
from datetime import date

def Bakups_ModelsTables(modeladmin, request, queryset):
    
    
    ruta = config('PATH_BACKUPS')
    content_type = ContentType.objects.get_for_model(queryset.model, for_concrete_model=False)
    name = content_type.name
    app = content_type.app_label
    schema = content_type.model
    print(app)
    print(schema)
    os.system('python manage.py dumpdata '+ app + '.' + schema + ' > ' + ruta  + schema + "-" + str(date.today())+ config('YAML'))

"""   
#Bakups_ModelsTables.short_description = "Backup Catalogo Menu"

class BakupsAdmin(admin.ModelAdmin):
    actions = [Bakups_ModelsTables]

"""
admin.site.add_action(Bakups_ModelsTables, "Backups")
admin.site.register(catalogoMenu)
admin.site.register(catalogoComponente)
admin.site.register(catalogoFuenteDatos)
admin.site.register(catalogoPerfil)
admin.site.register(catalogoPredictivo)


# Register your models here.
