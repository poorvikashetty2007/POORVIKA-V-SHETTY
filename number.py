def format_number(num, spec):
    result = format(num, spec)
    return result
output = format_number(145, 'o')
print("Formatted result:", output)
print("Representation used: Octal")
pi = 3.14
radius = 84
pond_area = pi * radius ** 2
print("Area of pond:", pond_area)
water_per_sq_meter = 1.4
total_water = pond_area * water_per_sq_meter
print("Total water in pond:", int(total_water), "liters")
distance = 490 
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("Speed in meters per second:", int(speed))