from django.db import models
from django.utils import timezone
from datetime import date
from rooms.models import Room
from authent.models import Users

#### PRECISA MIGRAR AINDA, DANDO ERRO STR
class Schedules(models.Model):
    room_reserved = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='schedules_created', null=True)
    
    def __str__(self):
        return f"{self.room_reserved} - {self.start_time} at {self.end_time}."