def time_conversion(s: str) -> str:
    number = int(s[:2])
    time = s[-2:]
    if time == 'PM' and number != 12:
        prefix = str(number + 12)
        res = prefix + s[2:-2]
    elif time == 'AM' and number == 12:
        res = '00' + s[2:-2]
    else:
        res = s[:-2]
    return res
