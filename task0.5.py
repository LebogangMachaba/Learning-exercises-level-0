def area_of_a_traingle(side_1, side_2, side_3):
    
    a = side_1
    b = side_2
    c = side_3

    p = (1/2*(a + b + c))

    area = ((p*(p-a)*(p-b)*(p-c)) ** (1/2))
    
    return area

area_of_a_traingle(6, 5, 5)
