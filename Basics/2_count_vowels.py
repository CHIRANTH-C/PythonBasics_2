# Assignment 2
# 2. Write a function named count_vowels that takes in a string as an argument and returns a dictionary that contains the count of each vowel (a, e, i, o, u) in the string.
"""
For example, if the input string is "Hello, world!", the function should return the following dictionary:```
{
    'a': 0,
    'e': 1,
    'i': 0,
    'o': 2,
    'u': 0
}
"""
def count_vowels(string_val):
   
    vowel_dict = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
    } # predefine the vowel dictionary and store 0 to all the vovels

    for key in vowel_dict.keys(): # itterate over the dictionary
     for char in string_val.lower(): # itterate over the string fetched from the console
         if key in char: # if the character match with the key of the dictionary
            vowel_dict[key] += 1 # add 1 to the value of the dictionary

    print(vowel_dict) # print the final result of vowel dictionary
        
count_vowels(input("Enter the string to calculate vowels : ")) # fetch the string value from the console and call the count_vowels function