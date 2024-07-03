from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes': notes})

def note_detail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'note/note_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note/note_create.html', {'form': form})

def note_edit(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/note_edit.html', {'form': form, 'note': note})

def note_delete(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note/note_confirm_delete.html', {'note': note})

def note_pin(request, id):
    note = get_object_or_404(Note, id=id)
    note.pinned = not note.pinned
    note.save()
    return redirect('note_list')

def note_move_up(request, id):
    note = get_object_or_404(Note, id=id)
    previous_note = Note.objects.filter(position__lt=note.position).order_by('-position').first()
    if previous_note:
        note.position, previous_note.position = previous_note.position, note.position
        note.save()
        previous_note.save()
    return redirect('note_list')

def note_move_down(request, id):
    note = get_object_or_404(Note, id=id)
    next_note = Note.objects.filter(position__gt=note.position).order_by('position').first()
    if next_note:
        note.position, next_note.position = next_note.position, note.position
        note.save()
        next_note.save()
    return redirect('note_list')