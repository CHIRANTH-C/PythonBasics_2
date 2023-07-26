number = [1,2,3,4,5,6,7,8,9] # declare the input list
odd_no_count = 0 # initialise the odd no count to 0
even_no_count = 0 # initialise the even no count to 0

for num in number: # itterate over the list
    if num % 2 == 0: # if num is completely divisible by 2
        even_no_count += 1 # add 1 to the even no count
    else:
        odd_no_count += 1 # else add 1 to odd numer count

print("odd numbers count are: ", odd_no_count) # print the odd no count result to console
print("even numbers count are: ", even_no_count) # print the even no count result to console