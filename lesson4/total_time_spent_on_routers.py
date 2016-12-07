trace_route_time = 75.0
phisical_distance = 2500.0
speed_of_light_in_optical_fiber = 200000.0

def calculate_total_time_spend_on_routers(trace_route_time,phisical_distance):
    speed_of_light_in_optical_fiber = 200000
    time_whithout_routers = (2*phisical_distance / speed_of_light_in_optical_fiber )*1000
    return trace_route_time - time_whithout_routers

print calculate_total_time_spend_on_routers(75.0, 2500.0)
