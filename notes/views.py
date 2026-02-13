from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "notes/index.html")


def add_note(request):
    return render(request, "notes/add.html")
