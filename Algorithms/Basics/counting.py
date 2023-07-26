# count of strings in a list that have a string length greater than 5

def word_counter():
# 1. Get input from the users , expecting coma seperated values of string (Eg : hi,this,good,number)
    user_input = input("Enter strings as csv: ")

# 2. Split the input with coma seperated and parse it to the list
    word_list = user_input.split(",")

# 3. count = 0
    count = 0

# 4. for loop over word list:
    for word in word_list:
# 5.    if len  of (string_no) > 5
        if len(word) > 5:
# 6.    add 1 to count
            count += 1

# 7. return count
        return count

result = word_counter()
print(result)