# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#
from lesson3.days_in_month import how_many_days


def convert_seconds(number_of_seconds):
    how_many_hours = int(number_of_seconds / 3600)
    how_many_minutes = int((number_of_seconds - how_many_hours*3600) / 60)
    how_many_seconds = (number_of_seconds - how_many_hours*3600 - how_many_minutes*60)

    if how_many_hours == 1:
        hours_form = "hour"
    else:
        hours_form = "hours"
    if how_many_minutes == 1:
        minutes_form = "minute"
    else:
        minutes_form = "minutes"
    if how_many_seconds == 1:
        seconds_form = "second"
    else:
        seconds_form = "seconds"
    return str(how_many_hours) + " " + hours_form + ", "+ str(how_many_minutes) + " " + minutes_form + ", " \
           + str(how_many_seconds) + " " + seconds_form

print convert_seconds(3661)
# >>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
# >>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
# >>> 2 hours, 1 minute, 1.7 seconds