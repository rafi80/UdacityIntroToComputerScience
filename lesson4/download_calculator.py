# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


def download_time(file_size, file_size_units, bandwidth, bandwidth_units):
    return convert_seconds(numberInMB(file_size, file_size_units) / numberInMB(bandwidth, bandwidth_units))


def numberInMB(inputNumber,unit):
    number_in_MBPs = {
        "MB": inputNumber,
        "Mb": (inputNumber*1.0/8),
        "kb": (inputNumber*1.0/(1024*8)),
        "kB": (inputNumber*1.0/(1024)),
        "Gb": (inputNumber*1.0*1024/8),
        "GB": (inputNumber*1.0*1024),
        "Tb": (inputNumber*1.0*1024*1024/8),
        "TB": (inputNumber*1.0*1024*1024)
    }
    return number_in_MBPs.get(unit, "nothing")


def convert_seconds(number_of_seconds):
    how_many_hours = int(number_of_seconds / 3600)
    how_many_minutes = int((number_of_seconds - how_many_hours*3600) / 60)
    how_many_seconds = (number_of_seconds - how_many_hours*3600. - how_many_minutes*60.)

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

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable