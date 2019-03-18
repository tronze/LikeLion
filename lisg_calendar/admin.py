from django.contrib import admin

# Register your models here.
from lisg_calendar.models import Event, Lesson, Absent

admin.site.register(Event)
admin.site.register(Lesson)
admin.site.register(Absent)
