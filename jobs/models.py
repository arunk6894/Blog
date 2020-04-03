from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=200)
    url1 = models.CharField(max_length=200)
    facultyname = models.CharField(max_length=100)