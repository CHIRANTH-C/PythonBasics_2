def max_value_of_sub_array():
    user_input = input("Enter strings as csv: ")
    num_list = user_input.split(",")
    int_list = []
    for i in num_list:
        int_list.append(int(i))
    
    max_val = int_list[0]
    max_last_val = int_list[0]
    for i in range(1, len(int_list)):
        max_last_val = max(int_list[i], max_last_val + int_list[i])
        max_val = max(max_val, max_last_val)
    return max_val

# 2,4,5,6,78,1

print(max_value_of_sub_array())
