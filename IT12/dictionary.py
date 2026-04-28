#Dictionary title / value

letters_of_the_alphabet = {
    '1st': 'a',
    '2nd': 'b',
    '3rd': 'c',
    '4th': 'd',
    '5th': 'e'
}

print(letters_of_the_alphabet.keys())
print(letters_of_the_alphabet.values())
print(letters_of_the_alphabet.items())
print(letters_of_the_alphabet.__getitem__('3rd'))

for key,value in letters_of_the_alphabet.items():
    print(f"The {key} letter of the alphabet is {value}")
