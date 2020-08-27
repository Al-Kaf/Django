from django.shortcuts import render , get_object_or_404
from notes_app.models import Note
# Create your views here.
from accounts.models import Profile


def allnotes(request):
    notes = Note.objects.all()
    if request.user.is_authenticated :
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        context = {
            'all_notes' : notes,
            'profile' : profile, 

        }
    else :
        context = {
            'all_notes' : notes, }

    return render(request, 'home.html', context )