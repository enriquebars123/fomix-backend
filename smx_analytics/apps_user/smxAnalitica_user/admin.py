from django.contrib import admin
from apps_user.smxAnalitica_user.models import (
    user,
    userArea,
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
    schema = content_type.models
    os.system('python manage.py dumpdata '+ app + '.' + schema + ' > ' + ruta  + schema +'.yaml')

admin.site.add_action(Bakups_ModelsTables, "Backups")
"""
admin.site.register(user)
admin.site.register(userArea)
