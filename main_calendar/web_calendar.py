from calendar import month_name, day_name, day_abbr

from django.utils.translation import ugettext_lazy as _

from lisg_calendar.models import Event
from main_calendar.web_elements.a import AElement
from main_calendar.web_elements.h1 import H1Element
from main_calendar.web_elements.table.th import ThElement
from main_calendar.web_elements.table.thead import TheadElement

from .base import BaseCalendar
from .web_elements.content import Content
from .web_elements.table.table import TableElement
from .web_elements.table.tbody import TbodyElement
from .web_elements.table.td import TdElement
from .web_elements.table.tr import TrElement
from .web_elements.web_classes import WebClasses


class WebCalendar(BaseCalendar):

    def __init__(self, year, month, firstweekday=6):
        super().__init__(year, firstweekday)
        self.month = month
        self.today_y = 0
        self.today_m = 0
        self.today_d = 0
        self.events = None

    def init_calendar_table(self, month):
        weeks = super().get_weeks(month)
        events = self.events

        table = TableElement()

        row_classname = WebClasses()
        row_classname.add_classname('row')
        row_classname.add_classname('m-0')
        col_classname = WebClasses()
        col_classname.add_classname('col')
        col_classname.add_classname('p-0')

        columns = list()
        # Print firstweekday to end of weekday first to format like a calendar.
        for dayname in range(self.firstweekday, len(day_name)):
            columns.append(day_abbr[dayname][0])
        # Print rest of the weekday before firstweekday.
        for dayname in range(0, self.firstweekday):
            columns.append(day_abbr[dayname][0])
        thead = TheadElement()
        tr = TrElement()
        tr.set_classnames(row_classname)
        for column in columns:
            th = ThElement()
            th.insert_node(Content(column))
            th.set_classnames(col_classname)
            tr.insert_node(th)
        thead.insert_node(tr)
        table.insert_node(thead)

        tbody = TbodyElement()
        # Print days except the situation when day is 0 as 0 means not a day in the month.
        for week in weeks:
            tr = TrElement()
            tr.set_classnames(row_classname)
            for day, weekday in week:
                td = TdElement()
                td.set_classnames(col_classname)
                # Print nothing for noday in month
                if day is 0:
                    td.insert_node(Content(""))
                # Print dates
                else:
                    td_classname = WebClasses()
                    td_classname.add_classname('col')
                    td_classname.add_classname('p-0')
                    td_classname.add_classname('active')
                    if day == self.today_d and self.month == self.today_m and self.year == self.today_y:
                        td_classname.add_classname('today')
                    a_tag = AElement()
                    a_classname = WebClasses()
                    a_tag.set_href("/calendar/events/" + str(self.year) + '-' + str(self.month) +'-' + str(day))
                    etext = ""
                    if events is not None:
                        elist = self.events.filter(datetime_info__day=day)
                        for event in elist:
                            etext += event.name + "<br>"
                    a_tag.insert_node(Content(str(day) + "<hr style='color: white; background-color: white; border-color: white;'>" + etext))
                    a_classname.add_classname("text-white")
                    a_tag.set_classnames(a_classname)
                    td.insert_node(a_tag)
                    td.set_classnames(td_classname)
                tr.insert_node(td)
            tbody.insert_node(tr)
        table.insert_node(tbody)
        classnames = WebClasses()
        classnames.add_classname("table")
        classnames.add_classname("table-bordered")
        classnames.add_classname("text-center")
        table.set_classnames(classnames)
        return table

    def get_calendar_month(self):
        return self.month

    def get_calendar_year(self):
        return self.year

    def get_info_div(self):
        h1 = H1Element()
        h1.insert_node(Content("%s, %s" % (_(month_name[self.month]), self.year)))
        return h1

    def get_calendar_table(self):
        return self.init_calendar_table(self.month)

    def set_today(self, year, month, day):
        self.today_y = year
        self.today_m = month
        self.today_d = day

    def set_events(self, events: Event):
        self.events = events
