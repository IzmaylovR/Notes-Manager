from django.conf.urls import url
from note.views import NoteCreate, NoteUpdate, NoteDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', 'note.views.notes'),
    url(r'note/add/$', 'note.views.NoteCreate'),
    url(r'note/update/$', 'note.views.NoteUpdate', name='NoteUpdate'),
    url(r'note/delete/$', 'note.views.NoteDelete', name='NoteDelete'),
    url(r'note/publish/$', 'note.views.NotePublish', name='NotePublish'),
    url(r'note/show/(?P<uuid>[^/]+)/$', 'note.views.NoteShow', name='NoteShow'),
    url(r'note/setFavourite/$', 'note.views.NoteSetFavourite', name='NoteSetFavourite'),
]
