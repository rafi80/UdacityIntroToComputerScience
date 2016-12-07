# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second


def speed_fraction(trace_route_time, physical_distance):
    communication_speed = (2 * physical_distance*1.0 / trace_route_time)*1000
    return communication_speed / speed_of_light


print speed_fraction(50, 5000)
#>>> 0.666666666667

print speed_fraction(50, 10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?

print speed_fraction(16, 20)
#>>> 0.00833333333333