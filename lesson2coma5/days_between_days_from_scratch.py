# coding=UTF-8
from math import floor

# napisać program, który obliczy ilość dni między dwoma datami bez wykorzystywania modulu date.
# zalozenie jest takie, że druga data podana w argumencie nie jest mniejsza od pierwszej


#Algortym:
# Do wejściowej daty startowej dodajemy jeden dzien i sprawdzamy, czy nie jest to data końcową.
# Jeżeli nie, dodajemy jeden dzien do wyniku i przesuwamy datę startową o jeden dzien w przyszłość


def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day+1
    else:
        if month<12:
            return year, month+1, 1
        else:
            return year+1,1,1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    daysBetween = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        daysBetween += 1
    return daysBetween


def dateIsBefore(year1, month1, day1, year2, month2, day2):

    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
        else:
            return False

def daysInMonth(year, month):

    if month in (1, 3,  5, 7, 8, 10, 12):
        return 31
    else:
        if month in (4, 6, 9, 11):
            return 30
        else:
            if isLeapYear(year):
                return 29
            else:
                return 28


def isLeapYear(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

#Tests
# print nextDay(2011,1,30)
# print nextDay(2011,12,30)
# print nextDay(2011,2,3)
# print nextDay(2011,9,29)

print daysBetweenDates(2013,1,1,2014,1,2)
print daysBetweenDates(2013,2,30,2013,3,1)
print daysBetweenDates(2013,12,30,2014,1,2)
print daysBetweenDates(2013,1,1,2013,3,3)
print daysBetweenDates(2013,1,1,2013,1,1)
print daysBetweenDates(2011, 1, 1, 2012, 8, 8)
print daysBetweenDates(1900, 1, 1, 1999, 12, 31)
# print daysBetweenDates(2013,1,1,2012,12,30)


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
