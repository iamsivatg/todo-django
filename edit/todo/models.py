from django.db import models

class Todoitem(models.Model):
    contents = models.TextField()
    #date_created = models.DateTimeField()
