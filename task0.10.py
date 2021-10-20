def common_letters():

    first_word = str(input("Please enter the first word: "))
    second_word = str(input("Please enter the second word: "))

    string_1 = set(first_word)
    string_2 = set(second_word)

    compare_letters = string_1 & string_2
    
    print(compare_letters)

common_letters()

