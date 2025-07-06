from django import forms
from .models import UploadedSong

class SongUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedSong
        fields = ['title', 'file']
