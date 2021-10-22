def extract_vowels(string):
    
    vowel_lst = ('aeoiuAEIOU')
    vowels = ''
    join_vowels = ", " 

    for v in string:
        if v not in vowels and v in vowel_lst :
             
            vowels = vowels.lower() + v   
                    
    print('Vowels: ',join_vowels.join(vowels))
extract_vowels('Umuzi'.lower())
