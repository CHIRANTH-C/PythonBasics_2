# Assignment 7

"""

7. Python program to find top two maximum number in a list.

"""

max1 = max2 = 0 # declare and initialise 0 to the max1 and max2 numbers
numbers = [3,4,5,6,6] # declare the list

for num in numbers: # itterate over the list
    if num > max1: # if num is greater 
        max2 = max1 # store max2 with what was there in max1
        max1 = num # store num to the max1
    elif num > max2 and num != max1: # else if num > max2 and num != max1
        max2 = num # store num to max2

print("Top 2 numbers are : ", max1 , max2) # print the top two numbers from the list to console

