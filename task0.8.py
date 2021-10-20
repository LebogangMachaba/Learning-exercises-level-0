number = int(input("Please enter number: "))
 
#convert number into hour(s) and minute(s) 
def convert_time(T):
    
    return number // 60
    print(T)

#calculate number of hours and remaining minutes

minutes = number % 60
hours = convert_time(number)

#making provision for plurals and singulars

if hours <= 1 and minutes <= 1:
    print(hours, " hour", minutes, "minute")
elif hours <= 1 and minutes > 1:
    print(hours, " hour", minutes, "minutes")
elif hours > 1 and minutes > 1:
    print(hours, " hours ", minutes, " minutes")
elif hours > 1 and minutes <= 1:
    print(hours, " hours ", minutes, " minute")



