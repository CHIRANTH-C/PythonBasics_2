def longest_common_subsequence_length():
    user_input = input("Enter 2 strings as csv: ")
    num_list = user_input.split(",")
    if num_list[0] > num_list[1]:
        S2 = num_list[0]
        S1 = num_list[1]
    else:
        S2 = num_list[1]
        S1 = num_list[0]

    M = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

    for i in range(1, len(S1) + 1):
        for j in range(1, len(S2) + 1):
            if S1[i-1] == S2[j-1]:
                M[i][j] = M[i-1][j-1] + 1
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])
    return M[len(S1)][len(S2)]

result = longest_common_subsequence_length()
print(f'The length of longest sub sequence from the given list of strings is {result}.')