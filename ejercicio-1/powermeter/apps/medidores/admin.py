from django.contrib import admin
from .models import Measurer, Measurement

# Register your models here.
class MeasurementAdmin(admin.ModelAdmin):
    #Permite ver la hora de creación de la medición en el panel Admin
    readonly_fields = ('created_at', )

admin.site.register(Measurer)
admin.site.register(Measurement,MeasurementAdmin)