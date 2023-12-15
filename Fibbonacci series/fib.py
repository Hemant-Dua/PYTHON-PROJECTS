# function for series
def fib_series (n):
    '''The number n will be taken and will give out it's fibonacci series till number n'''
    # 1st term is 0
    if (n==0):
        return 0
    # 2nd term is 1
    elif (n==1):
        return 1
    # nth term is [(n-1)th]+[(n-2)th] term   {//aka. Recursion}
    else:
        return (fib_series(n-1))+(fib_series(n-2))

# taking number from user
num=int(input("Enter number: "))

# if number is negative then error is generated
if (num<0):
    print("ERROR!!!")

# it calls for the function if number is natural
else:
    for n in range (num+1):
        print(fib_series(n))