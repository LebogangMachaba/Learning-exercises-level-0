#converts celsius to fahrenheit
def convert_to_fahrenheit(c):
    celsius = float(c)
    fahrenheit = float((9/5 * celsius) + 32)
    
    print("Your Celsius temperature in Fahrenheit is:", round(fahrenheit),"C")

convert_to_fahrenheit(33)

#converts fahrenheit to celsius
def convert_to_celsius(f):
    fahrenheit = float(f)
    celsius = float(5/9 *(fahrenheit - 32))
        
    print("Your Fahrenheit temperature in Celsius is:", round(celsius), 'F')  

convert_to_celsius(90)

