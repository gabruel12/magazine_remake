from django.db import models
from django.utils import timezone
from datetime import datetime
from rooms.models import Room
from authent.models import Users

class Schedules(models.Model):
    room_reserved = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_schedules')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='schedules_created')
    
    def __str__(self) -> str:
        start = self.start_time if self.start_time else "No have"
        end = self.end_time if self.end_time else "No have"
        return f"{self.room_reserved} - {start} at {end}."

    def save(self, *args, **kwargs):

        if not self.start_time and not self.end_time:
            self.start_time = datetime.now()
            self.end_time = datetime.now()

        super().save(*args, **kwargs)