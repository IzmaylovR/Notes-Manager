# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import uuid

class Note(models.Model):
    fields = ['note_title', 'note_text', 'note_date', 'note_category', 'note_favourite', 'note_id']
    class Meta:
        db_table = 'note'
    note_title = models.CharField(max_length=200)
    note_text = models.CharField(max_length=300)
    note_date = models.DateTimeField()
    CATEGORY_CHOICE = (
        ('link', 'Ссылка'),
        ('zametka', 'Заметка'),
        ('pamyatka', 'Памятка'),
        ('ToDo', 'ToDo'),
    )
    note_category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    note_favourite = models.BooleanField(default=False)
    note_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    note_published = models.BooleanField(default=False)
