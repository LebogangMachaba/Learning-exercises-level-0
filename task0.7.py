#collects input from user
celsius         = int(input("Please enter temperature in Celcius"))
fahrenheit_2    = int(input("Please enter temperature in Fahrenheit"))


#converts celsius to fahrenheit
def convert_to_fahrenheit(c):
    
    return (9/5 * celsius) + 32
    print(c)
fahrenheit = convert_to_fahrenheit(celsius)
print("Your Celsius temperature in Fahrenheit is:", fahrenheit)


#converts fahrenheit to celsius
def convert_to_celsius(f):

        return 5/9 *(fahrenheit_2 - 32)
        print(f)
celsius = convert_to_celsius(fahrenheit_2)  
print("Your Fahrenheit temperature in Celsius is", celsius)  

