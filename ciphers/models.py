import datetime
from django.db import models
from django.utils import timezone


class SavedDocs(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date_submitted = models.DateTimeField('document date')
    encrypted_text = models.TextField()
    notes = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return ' '.join([self.title, self.author])

