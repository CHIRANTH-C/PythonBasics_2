def binary_search(integer_list , target_result , low , high):

    mid = (low + high) // 2

    if target_result == integer_list[mid] :
        return mid
    
    if target_result < integer_list[mid] :
        high = mid - 1

    if target_result > integer_list[mid] :
        low = mid + 1
    
    return binary_search(integer_list , target_result , low , high)

sorted_list = list(range(1,23))
target_result = 22
low = 0
high = len(sorted_list) - 1
result_index = binary_search(sorted_list , target_result , low , high)

print(result_index)
print(sorted_list)