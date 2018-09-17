from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_due_on= models.DateTimeField(blank=False)
    owner = models.CharField(max_length=50)
    mark = models.BooleanField(default=False)