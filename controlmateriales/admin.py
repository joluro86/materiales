from django.contrib import admin
from import_export import resources
from controlmateriales.models import Guia, faltanteperseo, matfenix, matperseo, NumeroActa
from import_export.admin import ImportExportModelAdmin

class GuiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre_perseo', 'nombre_fenix')
admin.site.register(Guia, GuiaAdmin)

class ActaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(NumeroActa, ActaAdmin)

class MatfenixAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad')
admin.site.register(matfenix, MatfenixAdmin)     

class MatPerseoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad', 'acta')
admin.site.register(matperseo, MatPerseoAdmin)

class FaltantePerseoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad', 'acta','cantidad_fenix','diferencia')
admin.site.register(faltanteperseo, FaltantePerseoAdmin)



class FaltantePerseoResource(resources.ModelResource):
    class Meta:
        model = faltanteperseo

class PerseoResource(resources.ModelResource):
    class Meta:
        model = matperseo

class FenixResource(resources.ModelResource):
    class Meta:
        model = matfenix   
