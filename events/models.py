from django.db import models
from datetime import datetime

# Create your models here.
class Events(models.Model):
    event_title = models.CharField(max_length=250)
    event_date = models.DateTimeField('event date',default=datetime.now)
    event_location = models.CharField(max_length=250)
    event_description = models.TextField()

    def __str__(self):
        return self.event_title
    
