from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(default="Title", max_length=30)
    description = models.CharField(default="description", max_length=255)
    done = models.BooleanField(default=False)
