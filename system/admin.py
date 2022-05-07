from django.contrib import admin
from django import forms
from .models import Online, Server_log, Data, Antik_fup, Meeting, Setting

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


class Antik_fupAdminForm(forms.ModelForm):

    class Meta:
        model = Antik_fup
        fields = '__all__'

class Antik_fupAdmin(admin.ModelAdmin):
    form = Antik_fupAdminForm
    list_display = ['id','created_at','date','download','upload']
    readonly_fields = ['created_at']

admin.site.register(Antik_fup, Antik_fupAdmin)


class MeetingAdminForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = '__all__'


class MeetingAdmin(admin.ModelAdmin):
    form = MeetingAdminForm
    list_display = ['id','name','link','organizer','time',]
    readonly_fields = ['created_at']

admin.site.register(Meeting, MeetingAdmin)


class SettingForm(forms.ModelForm):

    class Meta:
        model = Setting
        fields = '__all__'


class SettingAdmin(admin.ModelAdmin):
    form = SettingForm
    list_display = ['id','name','data','notes']
    readonly_fields = ['created_at']

admin.site.register(Setting, SettingAdmin)