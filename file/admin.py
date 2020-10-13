from django.contrib import admin
from django import forms
from .models import Filer

class FilerAdminForm(forms.ModelForm):

    class Meta:
        model = Filer
        fields = '__all__'


class FilerAdmin(admin.ModelAdmin):
    form = FilerAdminForm
    list_display = ['title', 'created_by', 'created_at', 'size','upload','path']
    readonly_fields = ['created_at','title','size']

admin.site.register(Filer, FilerAdmin)


