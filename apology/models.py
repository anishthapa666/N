from django.db import models

class UploadedSong(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title
