def maximum(num_1, num_2, num_3 ):
    x = num_1
    y = num_2 
    z = num_3
    
    if y <= x >= z:
        return x
    elif x <= y >= z:
          return y
    elif y <= z >= x:
          return z



maximum(15, 10, 23)