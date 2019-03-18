from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    datetime_info = models.DateTimeField(default=timezone.localtime)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    absent_available = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.name + " - " + self.datetime_info.astimezone().strftime("%Y%m%d %H:%M")


class Lesson(Event):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=100)


class Absent(models.Model):
    absent_types = (
        (1, '결석'),
        (2, '지각'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    absent_type = models.PositiveSmallIntegerField(choices=absent_types, default=1)
    exemption = models.BooleanField(default=False)
    counted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.localtime)
