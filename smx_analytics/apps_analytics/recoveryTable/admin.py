from django.contrib import admin
from django.urls import path
from apps_analytics.recoveryTable.models import recoveryTable
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from smx_analytics.libraryBusiness.libUtility import utility
from decouple import config
import os


def recovery_ModelsTables(modeladmin, request, queryset):    
    ruta =  config('PATH_BACKUPS')
    items = queryset.values_list('nombre', flat=True)
    for catalogo in items:
        archivo = catalogo + config('YAML')
        #print(archivo)
        os.system('python manage.py loaddata ' + ruta + archivo)

recovery_ModelsTables.short_description = "Restore Models Table"

def delete_selected(modeladmin, request, queryset):
    items = queryset.values_list('nombre', flat=True)
    for item in items:
        print(item)
        recoveryTable.objects.filter(nombre=item).delete()
    
    """
    items = queryset.data 
    for yaml in items:
        print(yaml)
    
    #filename = yaml + ".xml"
    #print("entre")
    #print(filename)
    """

class BakupsAdmin(admin.ModelAdmin):
    change_list_template = "search_BackupTables.html"
    actions = [recovery_ModelsTables, delete_selected]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('backupTable/', self.search_BackupTables),
        ]
        return my_urls + urls

    def search_BackupTables(self, request):
        files = utility.search_file(self, config('PATH_BACKUPS'),config('YAML'))
        objs = []
        for TextFile in files:
            if not recoveryTable.objects.filter(nombre=TextFile).exists():
                objs.append(recoveryTable(nombre=TextFile)) 
        recoveryTable.objects.bulk_create(objs)
        self.message_user(request, "Busqueda de backups exitosa...  \"estas al dia\"")

        return HttpResponseRedirect("../")
        
# admin.site.add_action(Bakups_ModelsTables, "Backups")
#admin.site.disable_action("Bakups_ModelsTables")
#admin.site.disable_action('Backups')
admin.site.register(recoveryTable, BakupsAdmin)

# Register your models here.
