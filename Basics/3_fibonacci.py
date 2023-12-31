# Assignment 3
"""

3.Write a program that takes input of two numbers, say num_1 and num_2, it should generate the fibonacci numbers using these two as the starting point till the next 10 numbers
Example: 
If the input is 2 and 6 the output should be 2, 6, 8, 14, 22, 36, 58, 94, 152, 246   
If the input is 5 and -3 the output should be 5, -3, 2, -1, 1, 0, 1, 1, 2, 3

"""
def fibonacci(num_1 , num_2): # define a function called 'fibonacci()' that takes two variables as inputs 
  fibonacci_list = list() # create empty list called 'fibonacci_list'
  fibonacci_list.append(num_1) # append 1st number to the fibonacci_list
  fibonacci_list.append(num_2) # append 2nd number to the fibonacci_list
  while len(fibonacci_list)!= 10: # looping untill the fibonacci_list the size upto 10  
      next_fib_val = num_1 + num_2 # add 1st and 2nd number and store in next_fib_val
      fibonacci_list.append(next_fib_val) # append the next_fib_val to the fibonacci_list
      num_1 = num_2 # re-assing num_2 to num_1
      num_2 = next_fib_val # re-assing next_fib_val to num_2
  print(fibonacci_list) # print fibonacci_list
  resultString = ','.join(map(str, fibonacci_list)) # using map function creat each element in fibonacci_list to string
                                                   # and join all the converted string using coma ',' seperation
  print('1st 10 fibonacci result for input numbers are : '+resultString)

fibonacci(int(input('Enter 1st numbers : ')),int(input('Enter 2nd numbers : '))) # call high_score_word method and as the user to enter the string in console