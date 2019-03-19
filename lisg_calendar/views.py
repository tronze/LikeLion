from django.shortcuts import render
from django.utils import timezone
from django.utils.safestring import mark_safe

from lisg_calendar.models import Event
from main_calendar.web_calendar import WebCalendar

# Create your views here.


def display_simple_web_calendar(request):
    context = dict()
    today = timezone.localdate()
    if 'year' in request.GET:
        year = int(request.GET.get('year'))
    else:
        year = today.year
    if 'month' in request.GET:
        month = int(request.GET.get('month'))
        if month > 12:
            month = 12
        elif month < 1:
            month = 1
    else:
        month = today.month
    web_calendar = WebCalendar(year=year, month=month)
    events = Event.objects.filter(datetime_info__year=year, datetime_info__month=month).order_by('datetime_info')
    web_calendar.set_today(today.year, today.month, today.day)
    web_calendar.set_events(events)
    calendar = web_calendar.get_calendar_table()
    context['info'] = mark_safe(web_calendar.get_info_div().create_element())
    context['calendar'] = mark_safe(calendar.create_element())
    context['year'] = year
    context['month'] = month
    return render(request, 'lisg_calendar/main.html', context)


def display_events_by_date(request, date):
    context = dict()
    events = Event.objects.filter(datetime_info__date=date).order_by('datetime_info')
    context['events'] = events
    context['date_info'] = date
    return render(request, 'lisg_calendar/events.html', context)
