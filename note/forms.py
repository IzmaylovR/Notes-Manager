# -*- coding: utf-8 -*-
from django.forms import ModelForm
from note.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note_text', 'note_date', 'note_category', 'note_favourite']
