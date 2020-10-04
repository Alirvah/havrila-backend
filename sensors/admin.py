from django.contrib import admin
from django import forms
from .models import *

class SensorAdminForm(forms.ModelForm):

    class Meta:
        model = Sensor
        fields = '__all__'


class SensorAdmin(admin.ModelAdmin):
    form = SensorAdminForm
    list_display = ['ts', 'broadband','infrared','light','temprpi','temproom','pressure','humidity']
    readonly_fields = ['created_at']

admin.site.register(Sensor, SensorAdmin)


class StatusAdminForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = '__all__'


class StatusAdmin(admin.ModelAdmin):
    form = StatusAdminForm
    list_display = ['ts', 'uptime','cpu','mem','disk','temp','wrec','wtran']
    readonly_fields = ['created_at']

admin.site.register(Status, StatusAdmin)
