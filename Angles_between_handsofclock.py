def angle_between_hour_and_minute(hour, minute):
    if hour >= 12:
        hour = hour - 12
    minute_angle = minute * 6
    hour_angle = (hour * 30) + (minute * 0.5)
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

def angle_between_hour_and_second(hour, second):
    if hour >= 12:
        hour = hour - 12
    second_angle = second * 6
    hour_angle = hour * 30 + (second / 120)
    angle = abs(hour_angle - second_angle)
    return min(angle, 360 - angle)

def angle_between_minute_and_second(minute, second):
    minute_angle = minute * 6
    second_angle = second * 6
    angle = abs(minute_angle - second_angle)
    return min(angle, 360 - angle)

hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
second = int(input("Enter the second: "))

angle_hour_minute = angle_between_hour_and_minute(hour, minute)
angle_hour_second = angle_between_hour_and_second(hour, second)
angle_minute_second = angle_between_minute_and_second(minute, second)

print(f"The angle between the hour and minute hands is: {angle_hour_minute:.2f} degrees")
print(f"The angle between the hour and second hands is: {angle_hour_second:.2f} degrees")
print(f"The angle between the minute and second hands is: {angle_minute_second:.2f} degrees")
