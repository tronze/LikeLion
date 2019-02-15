from calendar import Calendar
from calendar import day_name
from calendar import month_name


class BaseCalendar(Calendar):

    def __init__(self, year, firstweekday=6):
        super().__init__(firstweekday)
        self.year = year

    def get_weeks(self, month):
        weeks = self.monthdays2calendar(year=self.year, month=month)
        return weeks

    def print_month(self, month):
        # Get month information
        weeks = self.get_weeks(month)
        # Print year, month information
        print("%s, %s" %(month_name[month], self.year))
        # Print firstweekday to end of weekday first to format like a calendar.
        for dayname in range(self.firstweekday, len(day_name)):
            print("%-8s" % day_name[dayname], end="\t")
        # Print rest of the weekday before firstweekday.
        for dayname in range(0, self.firstweekday):
            print("%-8s" % day_name[dayname], end='\t')
        print()
        # Print days except the situation when day is 0 as 0 means not a day in the month.
        for week in weeks:
            for day, weekday in week:
                # Print nothing for noday in month
                if day is 0:
                    print("%-8s" % "", end='\t')
                # Print dates
                else:
                    print("%-8s" % str(day).center(5), end='\t')
            print()
