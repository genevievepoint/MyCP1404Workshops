import random

def is_format_vaild(word_format):
    for character in word_format:
        if character != "c" and character != "v":
            return False
    return True

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Please enter the word format in 'c' or 'v': ")
while not is_format_vaild(word_format):
    print("PLease enter a valid format")
    word_format = input("Please enter the word format in 'c' or 'v': ")
word = ""
for kind in word_format:
   if kind == "c":
       word += random.choice(CONSONANTS)
   else:
       word += random.choice(VOWELS)
print(word)
