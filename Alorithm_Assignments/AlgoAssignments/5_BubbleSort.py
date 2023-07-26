def bubble_sort():
    user_input = input("Enter strings as csv: ")
    num_list = user_input.split(",")
    int_list = []
    for i in num_list:
        int_list.append(int(i))

    n = len(int_list)
    for i in range(n):
        # Last i elements are already in place
        for j in range(n - i - 1):
            # Traverse the num_listay from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
    print(int_list)

bubble_sort()
