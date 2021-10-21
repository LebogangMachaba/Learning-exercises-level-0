def extract_vowels(string):
    
    #declaring vowels
    Lcase_vowel = ['a', 'e', 'o', 'i', 'u'] 
    Ucase_vowel = ['A', 'E', 'I', 'O', 'U']
    
    vowels = []
    for v in string:
            if v in Lcase_vowel or v in Ucase_vowel == True:
                
                vowels.append(v)
    print('Vowels: ',(vowels), end= '' )

extract_vowels('Umuzi')



