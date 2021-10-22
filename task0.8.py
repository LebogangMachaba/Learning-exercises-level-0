def convert_time(T):
    minutes = T % 60
    hours = T // 60
    

    if hours <= 1 and minutes <= 1:
        print(hours, " hour", minutes, "minute")
    elif hours <= 1 and minutes > 1:
        print(hours, " hour", minutes, "minutes")
    elif hours > 1 and minutes > 1:
        print(hours, " hours ", minutes, " minutes")
    elif hours > 1 and minutes <= 1:
        print(hours, " hours ", minutes, " minute")

convert_time(119)

