input_list = input("Enter CSV numbers")

seperated_input = input_list.split(',')
int_list = []

for entry in seperated_input:
    int_list.append(int(entry))

def quick_sort(integer_list):
    if len(integer_list) <= 1:
        return integer_list
    
    pivot_index = (len(integer_list) - 1) // 2

    pivot = integer_list[pivot_index]

    small_list , middle_list , bigger_list = [] , [] , []

    for element in integer_list:
        if element == pivot:
            middle_list.append(element)
        
        if element < pivot:
            small_list.append(element)

        if element > pivot:
            bigger_list.append(element)

    return quick_sort(small_list) + middle_list + quick_sort(bigger_list)

sorted_list = quick_sort(int_list)
print(sorted_list)
