# sum of values in a list that are even - sum of values in a list that are odd

# Step 1 : Get the list of number from the inputs in form of csv
def summing():
    input_list = input("Enter the csv numbers : ")

    if not input_list:
        return None

    # Step 2 : Parse it to a list of numbers
    number_list = input_list.split(',')
    print(number_list)

    # Step 3 : even_no = 0
    even_sum = 0

    # Step 4 : odd_no = 0
    odd_sum = 0

    # Step 5 : values_no = 0
    value_sum = 0

    # Step 6 : Loop through over the list one by one
    for num in number_list:
    # Step 7 : Check if num is completely divisible by 2
        if int(num) % 2 == 0:
    # Step 8 : If yes add num to even_no
            even_sum += int(num)
    # Step 9 : Else 
        else:
    # Step 10 : Add num to odd_no
            odd_sum += int(num)

    # Step 11 : value_no = even_no - odd_no
    value_sum = even_sum - odd_sum
    print(even_sum)
    print(odd_sum)
    print(value_sum)

summing()