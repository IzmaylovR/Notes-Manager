from django.contrib import admin
from note.models import Note


# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    fields = ['note_title', 'note_text', 'note_date', 'note_category', 'note_favourite']
    list_filter = ['note_title', 'note_date', 'note_category', 'note_favourite']


admin.site.register(Note, NoteAdmin)
