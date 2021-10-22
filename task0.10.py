def common_letters(first_word, second_word):
    string_1 = first_word
    string_2 = second_word
    
    common_letters = ', '
    output = ''
    for letter in first_word and second_word:

        if letter in string_1 and letter in string_2:
            output = output + letter
        
    
    print('Common Letters:', common_letters.join(output))

common_letters('Houses', 'Computers')

