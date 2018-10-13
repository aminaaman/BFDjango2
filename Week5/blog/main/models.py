from django.db import models

# Create your models here.

class User(models.Model):
    handle = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Comment(models.Model):
    text = models.TextField()
    commenter = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateField()

class Post(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    body = models.TextField()
    created = models.DateField()
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)


