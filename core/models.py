from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 30)
    date = models.DateField()
    lead = models.CharField(max_length = 30, blank = True)
    text = models.TextField()