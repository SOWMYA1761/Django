from django.db import models

class reports(models.Model):
    place = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

def __str__(self):
    return self.place