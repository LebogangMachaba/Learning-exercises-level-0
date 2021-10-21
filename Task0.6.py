def maximum(num_1, num_2, num_3 ):
    x = num_1
    y = num_2 
    z = num_3
    
    if y <= x >= z:
        print("The Maximum number is", x)
    elif x <= y >= z:
          print("The Maximum number is", y)
    elif y <= z >= x:
          print("The Maximum number is", z)



maximum(15, 10, 23)