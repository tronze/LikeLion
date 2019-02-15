from django.shortcuts import render
from django.utils.safestring import mark_safe

from main_calendar.web_calendar import WebCalendar

# Create your views here.


def display_simple_web_calendar(request):
    context = dict()
    web_calendar = WebCalendar(year=2019)
    if 'month' in request.GET:
        month = (lambda a: a if a > 0 else 1)(request.GET.get('month'))
        context['calendar'] = mark_safe(web_calendar.print_calendar_table(month))
    else:
        context['calendar'] = mark_safe(web_calendar.print_calendar_table(1))
    return render(request, 'lisg_calendar/main.html', context)
