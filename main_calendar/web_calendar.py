from calendar import month_name, day_name

from main_calendar.web_elements.table.th import ThElement
from main_calendar.web_elements.table.thead import TheadElement
from .base import BaseCalendar
from .web_elements.content import Content
from .web_elements.div import DivElement
from .web_elements.table.table import TableElement
from .web_elements.table.tbody import TbodyElement
from .web_elements.table.td import TdElement
from .web_elements.table.tr import TrElement
from .web_elements.web_classes import WebClasses


class WebCalendar(BaseCalendar):

    def __init__(self, year, firstweekday=6):
        super().__init__(year, firstweekday)

    def print_calendar_table(self, month):
        weeks = super().get_weeks(month)

        div = DivElement()
        div.insert_node(Content("%s, %s" % (month_name[month], self.year)))

        table = TableElement()

        row_classname = WebClasses()
        row_classname.add_classname('row')
        row_classname.add_classname('m-0')
        col_classname = WebClasses()
        col_classname.add_classname('col')

        columns = list()
        # Print firstweekday to end of weekday first to format like a calendar.
        for dayname in range(self.firstweekday, len(day_name)):
            columns.append(day_name[dayname])
        # Print rest of the weekday before firstweekday.
        for dayname in range(0, self.firstweekday):
            columns.append(day_name[dayname])
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
                    td.insert_node(Content(str(day)))
                tr.insert_node(td)
            tbody.insert_node(tr)
        table.insert_node(tbody)
        classnames = WebClasses()
        classnames.add_classname("table")
        classnames.add_classname("table-bordered")
        classnames.add_classname("text-center")
        table.set_classnames(classnames)
        return div.create_element() + table.create_element()
