from datetime import date, timedelta

class Nineteen(object):
    """
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
    divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to
    31 Dec 2000)?
    """

    def __init__(self, starting_date, end_date):
        self.starting_date = starting_date
        self.end_date = end_date

    def date_is_a_sunday(self, date):
        day_of_week = date.isoweekday()
        if day_of_week == 7:
            return True
        else:
            return False

    def date_is_first_of_the_month(self, date):
        calendar_day = date.day
        if calendar_day == 1:
            return True
        else:
            return False

    def collect_sundays_that_are_first_of_month(self, starting_date, end_date):
        list_of_first_of_the_month_sundays = []
        current_date = starting_date
        while current_date <= end_date:
            if self.date_is_first_of_the_month(current_date):
                if self.date_is_a_sunday(current_date):
                    list_of_first_of_the_month_sundays.append(current_date)
                    current_date += timedelta(days=27)
                else:
                    current_date += timedelta(days=27)
            else:
                current_date += timedelta(days=1)
        return len(list_of_first_of_the_month_sundays)

    def solve(self):
        result = self.collect_sundays_that_are_first_of_month(self.starting_date, self.end_date)
        return result


starting_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

nineteen = Nineteen(starting_date, end_date)
print(nineteen.solve())



