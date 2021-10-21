def area_of_a_traingle(side_1, side_2, side_3):
    
    a = side_1
    b = side_2
    c = side_3

    #formula for area using 3 sides as per https://www.wikihow.com/Calculate-the-Area-of-a-Triangle
    area = 1/2*(a + b + c)
    return area
    
    print("The Area of your Triangle is:", + area)

area_of_a_traingle(5, 4, 3)
