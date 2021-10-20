


def maximum():
    num_1 = int(input("Please Enter 1st Number:"))
    num_2 = int(input("Please Enter 2nd Number:"))
    num_3 = int(input("Please Enter 3rd Number:"))
    
    if num_2 <= num_1 >= num_3:
        print("The Maximum number is", num_1)
    elif num_1 <= num_2 >= num_3:
          print("The Maximum number is", num_2)
    elif num_2 <= num_3 >= num_1:
          print("The Maximum number is", num_3)



maximum()