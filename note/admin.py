from django.contrib import admin
from django import forms
from .models import Notebook
from .models import Note

class NotebookAdminForm(forms.ModelForm):

    class Meta:
        model = Notebook
        fields = '__all__'


class NotebookAdmin(admin.ModelAdmin):
    form = NotebookAdminForm
    list_display = ['title', 'created_by', 'created_at']
    readonly_fields = ['created_at']

admin.site.register(Notebook, NotebookAdmin)


class NoteAdminForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'


class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm
    list_display = ['title','notebook','starred','created_at']
    readonly_fields = ['created_at']

admin.site.register(Note, NoteAdmin)


# Register your models here.
