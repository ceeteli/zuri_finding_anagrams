# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

first_word = input('Enter the first word here: ')
second_word = input('Enter the second word here: ')
    


def find_anagrams(first_word, second_word):
    # [assignment] Add your code here
    
    if sorted(first_word) == sorted(second_word) and len(sorted(first_word))==len(sorted(second_word)):
        return True
    else:
        return False

print(find_anagrams(first_word, second_word))
