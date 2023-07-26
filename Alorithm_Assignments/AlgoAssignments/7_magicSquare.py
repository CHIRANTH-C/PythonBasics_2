def generate_magic_square(n):
    magic_square = [[0 for x in range(n)] for y in range(n)]
    i, j = 0, n//2
    for num in range(1, n**2+1):
        magic_square[i][j] = num
        next_i, next_j = (i-1)%n, (j+1)%n
        if magic_square[next_i][next_j]:
            i = (i+1)%n
        else:
            i, j = next_i, next_j

    print("The magic square is:")
    for i in range(n):
        for j in range(n):
            print(magic_square[i][j], end=" ")
        print()


# Print the magic square
input_num = int(input("Enter the size of the magic square: "))
generate_magic_square(input_num)