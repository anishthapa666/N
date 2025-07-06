from django.shortcuts import render , redirect

# Create your views here.


def home(request):
    return render(request, 'apology/home.html')

def memories(request):
    return render(request, 'apology/memories.html')

def reasons(request):
    reasons_list = [
        "Your smile makes my day",
        "You always support me even when I mess up",
        "You're my favorite person to talk to",
        "You're strong, kind, and beautiful"
    ]
    return render(request, 'apology/reasons.html', {'reasons': reasons_list})

def forgive(request):
    return render(request, 'apology/forgive.html')
# from .models import DiaryEntry

# def diary(request):
#     entries = DiaryEntry.objects.order_by('-created_at')
#     return render(request, 'apology/diary.html', {'entries': entries})

# def music(request):
#     return render(request,'apology/music.html')
from .forms import SongUploadForm
from .models import UploadedSong

def music_upload(request):
    song = None
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save()
    else:
        form = SongUploadForm()
    return render(request, 'apology/music_upload.html', {'form': form, 'song': song})

def YES(request):
    return render(request, 'apology/yes.html')

def NO(request):
    return render(request, 'apology/no.html')

def letter_view(request):
    return render(request, 'apology/letter.html')