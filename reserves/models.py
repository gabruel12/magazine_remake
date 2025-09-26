from django.db import models
from django.utils import timezone
from datetime import date
from rooms.models import Room

class Schedules(models.Model):
    room_reserved = models.ForeignKey(Room, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.room_reserved