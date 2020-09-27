from django.contrib import admin
from django import forms
from .models import Device

class WifiAdminForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = '__all__'


class WifiAdmin(admin.ModelAdmin):
    form = WifiAdminForm
    list_display = ['created_at', 'name','ip','mac']
    readonly_fields = ['created_at']

admin.site.register(Device, WifiAdmin)


# Register your models here.
