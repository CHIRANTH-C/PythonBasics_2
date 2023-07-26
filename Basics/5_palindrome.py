# Assignment 5

"""

5. Write a python program that takes a string, converts it into a list and converts it into a palindrome by creating a copy of the list and concatenating both strings.

example: 

	if string_example = "programmer"

	list1 = list(example) # ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r']

	list2 should be reverse of list1

	output should be letters of list1 + list2 so that it forms a palindrome.

Use the join() function to achieve this.

"""

string_example = "programmer" # initialise the string variable and assign the string value
list1 = list(string_example) # convert the string to list and assign it to list1
list2 = list() # cerate an empty list2
print(list1) # print the 1st list1
for i in range(len(list1)): # start looping on the list and itterate on each value of the list
     last_item = list1.pop() # extract the last value of this list using pop function and store it in a variable called last_item
     list2.insert(i, last_item) # insert these elements that gets extracted to list2
print(list2) # print the reversed list value
rev_of_string_example = "".join(list2) # join each character in the list2 and save it as a string in rev_of_string_example variable
print(rev_of_string_example) # print the reversed string
result = string_example+rev_of_string_example # concatinate two string both actual and reversed to get a palindrome string
print("result : "+result) # print the palindrome result to the console