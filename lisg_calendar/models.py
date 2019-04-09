import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
from LikeLion import utils


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
    materials = models.FileField(upload_to=utils.custom_path, blank=True)


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


class Alarm(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    aid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    alarm_dt = models.DateTimeField()
    receivers = models.ManyToManyField(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return "[%s]" % self.alarm_dt.astimezone().strftime("%Y년 %m월 %d일 %H시 %M분")
