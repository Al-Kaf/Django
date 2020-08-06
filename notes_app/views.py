from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.


def all_notes(request):
    #return HttpResponse('<h1> Welcome</h1>')
    all_notes = Note.objects.all()
    context = {
        'all_notes' : all_notes
    }
    return render(request, 'all_nodes.html', context)


def detail(request, slug):
    note = Note.objects.get(slug = slug)
    context = {
        'note' : note
    }
    return render(request, 'node_detail.html', context)