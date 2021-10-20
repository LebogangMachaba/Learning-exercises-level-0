def extract_vowels(string):
    
    #declaring vowels
    vowel = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'I', 'O', 'U']
    for v in string:
        if v in vowel:
            string = vowel
            print("Vowels: ", v )

extract_vowels('Umuzi')



