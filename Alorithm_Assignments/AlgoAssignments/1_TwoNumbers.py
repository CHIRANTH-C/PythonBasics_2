def two_sum():
    user_input = input("Enter strings as csv: ")
    num_list = user_input.split(",")
    int_list = []
    for i in num_list:
        int_list.append(int(i))

    target_input = int(input("Enter target"))


    num_dict = {}
    for i in range(len(int_list)):
        diff = target_input - int_list[i]
        print(diff)
        if diff in num_dict:
            return [num_dict[diff], i]
        num_dict[int_list[i]] = i
        print(num_dict)
    return []


n = [1,2,3,4,5,6]
target = 10
result = two_sum()
print(result)