def format_duration(seconds):
    if seconds == 0:
        return 'now'
    second = seconds % 10
    minute = seconds // 60 % 60
    hour = seconds // 3600
    day = seconds // 86400 % 365
    year = seconds // 31536000

    lst = []

    if year >= 2:
        lst.append(str(year) + " years")
    if day == 1:
        lst.append("1 day, ")
    if day >= 2:
        lst.append(f"{day} days, ")
    if 2 > hour > 0:
        lst.append("1 hour, ")
    if hour > 1:
        lst.append(f"{hour} hours, ")
    if 2 > minute > 0:
        lst.append("1 minute, ")
    if second == 1:
        lst.append("1 second")
    if seconds > 2:
        lst.append(f"{second} seconds")
    return lst


print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
