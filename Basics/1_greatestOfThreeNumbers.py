# Assignment 1 -
# 1. Write a program in Python to find greatest among three integers.
number_1 = int(input("Enter the 1st number : ")) # get the number from the console
number_2 = int(input("Enter the 2nd number : ")) # get the number from the console
number_3 = int(input("Enter the 3rd number : ")) # get the number from the console

if number_1 > number_2 : # if 1st number is greater
    great_num = number_1 # store that number is great_num variable
else :
    great_num = number_2 # else store the 2nd number in great_num variable

if great_num > number_3 : # if great num is greater
    greatest_num = great_num # store that number in greatest_mun variable
else :
    greatest_num = number_3 # else store 3rd number in greatest_num variable

print("Greatest number among 3 numbers is " + str(greatest_num)) # print the greatest number result to the console