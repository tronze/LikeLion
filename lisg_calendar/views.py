from django.shortcuts import render
from django.utils.safestring import mark_safe

from lisg_calendar.models import Event
from main_calendar.web_calendar import WebCalendar

# Create your views here.


def display_simple_web_calendar(request):
    context = dict()
    web_calendar = WebCalendar(year=2019, month=2)
    calendar = web_calendar.get_calendar_table()
    context['info'] = mark_safe(web_calendar.get_info_div().create_element())
    context['calendar'] = mark_safe(calendar.create_element())
    return render(request, 'lisg_calendar/main.html', context)


def display_events_by_date(request, date):
    context = dict()
    events = Event.objects.filter(datetime_info__date=date)
    context['events'] = events
    context['date_info'] = date
    return render(request, 'lisg_calendar/events.html', context)
