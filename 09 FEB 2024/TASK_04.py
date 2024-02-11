# Fibonacci series ==> 0, 1, 2, 3, 5, 8, 13
# first will take two inputs
a = 0
b = 1
for i in range(10):
    #  will find the third number using the below one
    c = a + b
    # then will change the last two variables (the last of the second is equal to the last one, like a=b).
    a = b
    # The last one is equal to the new one.
    b = c
    # print the third number in row
    print(c, end=' ')
