from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def index(request):
    notes = Note.objects.all().order_by('-id')
    return render(request, "notes/index.html", {
        "notes": notes
    })


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data added successfully!')
            return redirect('notes:index')
        else:
            form = NoteForm()
    return render(request, "notes/add.html", {
        "form": NoteForm()
    })


def edit_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note.title = form.cleaned_data['title']
            note.description = form.cleaned_data['description']
            note.save()
            messages.success(request, 'Data updated successfully!')
            return redirect('notes:index')
    else:
        initial_data = {
            'title': note.title,
            'description': note.description
        }
        form = NoteForm(initial=initial_data)

    return render(request, "notes/add.html", {
        "form": form
    })


def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('notes:index')
