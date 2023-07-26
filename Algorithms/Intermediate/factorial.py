# Step 1 : input of n
input_n = input("Enter the input value : ")
 
# Step 2 : type cast n to int
converted_int = int(input_n)

# Step 3 : function factorial(n):
def factorial(n):

# Step 4 : if n is 0 or n is 1 :
    if n == 1 or n == 1:

# Step 5 : return 1
        return 1

# Step 6 : factorial_result = n * factorial(n-1) <- recursive function call is happening    
    factorial_result = n * factorial(n-1)

# Step 7 : return factorial_result
    return factorial_result

result = factorial(converted_int)

# Step 8 : print factorial(n)
print(result)