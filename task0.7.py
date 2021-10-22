def celsius_to_fahrenheit(c):
    celsius = float(c)
    fahrenheit = float((9/5 * celsius) + 32)
    
    return fahrenheit

celsius_to_fahrenheit(33)


def fahrenheit_to_celsius(f):
    fahrenheit = float(f)
    celsius = float(5/9 *(fahrenheit - 32))
        
    return celsius 

fahrenheit_to_celsius(90)

