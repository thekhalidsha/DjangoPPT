# presentation_app/models.py
from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField()
