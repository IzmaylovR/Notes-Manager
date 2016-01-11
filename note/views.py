from django.shortcuts import render_to_response
from note.models import Note
from note.forms import NoteForm
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def notes(request):
    notes = Note.objects.filter(created_by_id=request.user)
    return render_to_response('notes.html', {'request': request,
                                             'notes': notes,
                                             'username': auth.get_user(request).username})

@login_required
def NoteCreate(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            # return redirect('/')
            return HttpResponseRedirect('/')
    else:
        form = NoteForm()

    return render(request, 'note_create.html', {'form': form})

@login_required
def NoteUpdate(request):
    noteid = request.GET['id']
    note = Note.objects.get(id=noteid)
    form = NoteForm(request.POST or None, instance=note)
    if request.method == 'POST':
        if form.is_valid():
            note.save()
            # return redirect('/')
            return HttpResponseRedirect('/')
    else:
        return render(request, 'note_create.html', {'form': form})

@login_required
def NoteDelete(request):
    if request.method == 'GET':
        noteid = request.GET['id']
        Note.objects.filter(id=noteid).delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Request is invalid')

@login_required
def NotePublish(request):
    if request.method == 'GET':
        # username = request.POST['username']
        id = request.GET['id']
        note = Note.objects.get(id=id)
        note.note_published = not note.note_published
        note.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Request is invalid')

def NoteShow(request, uuid):
    note = Note.objects.get(note_uuid=uuid)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        note.save()
        return HttpResponseRedirect('/')
    return render(request, 'note_create.html', {'form': form})

def NoteSetFavourite(request):
    id = request.POST['id']
    note = Note.objects.get(id=id)
    note.note_favourite = not note.note_favourite
    note.save()
    return HttpResponse(1)



