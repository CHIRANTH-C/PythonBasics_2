# Assignment 6

"""

6. Python program to find the average of numbers

For example:

Case1: If the user input the sequence 1,2,3,4,5,6,7,8,9.

then the output should be 5.

Case2: If the user input the sequence 11,22,33,44,55,66,77,88,99.

then the output should be 55.



"""

list_of_numbers = input("Enter the numbers in a comma seperated value formate : ") # fetch the numbers from the console
number_in_list_form = list_of_numbers.split(",") # split the number using coma seperation and store it in a list
sum = 0 # declare a sum variable and initialise it with 0
for num in number_in_list_form: # itterate over the list
    sum += int(num) # add all the values in the list
    average = sum / len(number_in_list_form) # find the average of the values in list

print("average of input numbers is : "+ str(average)) # print the obtained result in console