from django.shortcuts import render
from django.utils.safestring import mark_safe

from main_calendar.web_calendar import WebCalendar

# Create your views here.


def display_simple_web_calendar(request):
    context = dict()
    web_calendar = WebCalendar(year=2019)
    context['calendar'] = mark_safe(web_calendar.print_calendar_table(3))
    return render(request, 'lisg_calendar/main.html', context)
