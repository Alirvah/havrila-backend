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