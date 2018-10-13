from django.db import models

# Create your models here.
from django.db.models import CharField

class Task(models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateField()
    due_to = models.DateField()
    owner = models.CharField(max_length = 100)
    mark = models.BooleanField()
    def __str__(self):
        return '{} {}'.format(self.name, self.owner)



