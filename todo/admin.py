from django.contrib import admin
from django import forms
from .models import Todo

class TodoAdminForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'


class TodoAdmin(admin.ModelAdmin):
    form = TodoAdminForm
    list_display = ['title', 'created_by', 'created_at', 'done']
    readonly_fields = ['created_at']

admin.site.register(Todo, TodoAdmin)

