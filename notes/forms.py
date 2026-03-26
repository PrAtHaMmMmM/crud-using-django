from django import forms
from .models import Note


class NoteForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea, min_length=10)

    def save(self):
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        note = Note(title=title, description=description)
        note.save()
        return note
