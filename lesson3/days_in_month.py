days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(month):
    return days_in_month[month-1]




print how_many_days(1)
print how_many_days(2)
print how_many_days(3)
print how_many_days(4)
print how_many_days(5)
print how_many_days(6)
print how_many_days(7)
print how_many_days(8)
print how_many_days(9)
print how_many_days(10)
print how_many_days(11)
print how_many_days(12)


def test():
    assert how_many_days(3) == 31
    assert how_many_days(2) == 28
    print 'Tests finished'

test()