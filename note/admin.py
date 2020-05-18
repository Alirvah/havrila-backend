from django.contrib import admin
from django import forms
from .models import Note

class NoteAdminForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'


class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm
    list_display = ['title', 'content', 'created_by', 'starred']
    #readonly_fields = ['name', 'size']

admin.site.register(Note, NoteAdmin)


# Register your models here.
