import datetime

from django.db import models
from django.utils import timezone

class HTestResults(models.Model):
    string_A = models.CharField(max_length=200)
    string_B = models.CharField(max_length=200)
    hdistance = models.IntegerField(default=0)
    log_htest = models.DateTimeField('date of test')

    def __str__(self):
        return ' '.join([self.string_A, self.string_B])
