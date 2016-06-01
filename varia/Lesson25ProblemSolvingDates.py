'''
Created on 18 wrz 2013

@author: Stefan
'''
def isLeapYear(year):
    if year % 400 ==0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print isLeapYear(2012)

def daysInMonth(month,year):
    assert month < 13

    if month==1:
        return 31
    if month==3:
        return 31
    if month==4:
        return 30
    if month==5:
        return 31
    if month==6:
        return 30
    if month==7:
        return 31
    if month==8:
        return 31
    if month==9:
        return 30
    if month==10:
        return 31
    if month==11:
        return 30
    if month==12:
        return 31
    if month==2 and isLeapYear(year)==True:
        return 29
    else:
        return 28

print daysInMonth(6, 2012)

#===============================================================================
# def nextDay(year,month, day):
#     nextDay = day
#     nextMonth =month
#     nextYear=year
#     if day==30:
#         nextDay = 1
#         if month == 12:
#             nextMonth = 1
#             nextYear = year + 1
#         else:
#             nextMonth = month + 1
#     else:
#         nextDay = day+1 
#     return nextYear, nextMonth, nextDay
#===============================================================================

def nextDay(year, month, day):
    if day < daysInMonth(month,year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
print nextDay(2011, 6, 30)
print nextDay(1999, 12, 30)
print nextDay(2013, 1, 30)
print nextDay(2012, 12, 30)
#===============================================================================
# def dateIsBefore(year1, month1, day1,year2,month2,day2):
#     if year1>year2:
#         return False
#     elif year1==year2:
#         if month1>=month2 and day1>=day2:
#             return False
#         else:
#             return True 
#===============================================================================

def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False  
    
print dateIsAfter(2012, 12, 30,2012,12, 30)        
print dateIsAfter(2013, 1, 1,2012,12, 30)   
print dateIsAfter(2012, 12, 29,2012,12, 30)   


#===============================================================================
# def daysBeetweenDates(year1, month1, day1,year2,month2,day2):
#     daysBeetweenDates = 1
#     if (year1, month1, day1) == (year2,month2,day2):
#         return 0
#     elif (year2,month2,day2)== nextDay(year1, month1, day1):
#         return 1
#     else:
#         while nextDay(year1, month1,day1)<>(year2,month2,day2):
#             (year1,month1,day1)=nextDay(year1,month1,day1)
#             daysBeetweenDates += 1
#         return daysBeetweenDates
#===============================================================================
    
def daysBeetweenDates(year1, month1, day1,year2,month2,day2):
    assert not dateIsAfter(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days
           
print daysBeetweenDates(2011, 6, 30, 2012, 6, 30)

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBeetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"
            
test()
