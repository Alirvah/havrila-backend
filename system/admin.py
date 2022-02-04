from django.contrib import admin
from django import forms
from .models import *

class OnlineAdminForm(forms.ModelForm):

    class Meta:
        model = Online
        fields = '__all__'

class OnlineAdmin(admin.ModelAdmin):
    form = OnlineAdminForm
    list_display = ['id','created_at', 'name','last_updated']
    readonly_fields = ['created_at']

admin.site.register(Online, OnlineAdmin)



class Server_logAdminForm(forms.ModelForm):

    class Meta:
        model = Server_log
        fields = '__all__'

class Server_logAdmin(admin.ModelAdmin):
    form = Server_logAdminForm
    list_display = ['id','created_at', 'name','last_updated','user','operation','server']
    readonly_fields = ['created_at']

admin.site.register(Server_log, Server_logAdmin)


class DataAdminForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = '__all__'

class DataAdmin(admin.ModelAdmin):
    form = DataAdminForm
    list_display = ['id','created_at', 'name','last_updated','data']
    readonly_fields = ['created_at']

admin.site.register(Data, DataAdmin)