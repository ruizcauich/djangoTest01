from django.db import models
from datetime import datetime

# Create your models here.
#clase to do, del video
class Todo(models.Model):
    title = models.CharField(max_length =200)
    text = models.TextField()
    created_at = models.DateTimeField( default =  datetime.now, blank = True )

    def __str__(self):
        return self.title
