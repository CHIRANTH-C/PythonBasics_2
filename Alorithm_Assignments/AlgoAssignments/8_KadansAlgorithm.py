def kadane():
    user_input = input("Enter strings as csv: ")
    num_list = user_input.split(",")
    int_list = []
    for i in num_list:
        int_list.append(int(i))

    max_so_far = 0
    max_ending_here = 0
    
    for i in range(len(int_list)):
        max_ending_here += int_list[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            
    return max_so_far

max_subint_listay_sum = kadane()
print(max_subint_listay_sum)