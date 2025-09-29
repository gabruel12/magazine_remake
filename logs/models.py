from django.db import models
from datetime import date
from django.utils import timezone

class Log(models.Model):
    text = models.TextField(max_length=255)
    datetime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.text}: {self.datetime}"

    def save(self, *args, **kwargs):
        self.datatime = datetime.now()

        super().save(*args, **kwargs)
    
# def -> {thing} -> {message} --> create a log in Logs

def logger(message: str, **kwargs):
    from logs.logs_msg import LOGS_MESSAGES
    template_message = LOGS_MESSAGES.get(message)
    if not template_message:
        raise ValueError(f"The message key '{message}' dont was searched in LOGS_MESSAGES.")
    formatted_message = template_message.format(**kwargs)
    Log.objects.create(text=formatted_message)