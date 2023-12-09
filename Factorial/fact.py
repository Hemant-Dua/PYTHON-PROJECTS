# function for factorial
def factorial(n):
    # if n is not equal to 0 then this formula
    if n!=0:
        return (factorial(n-1)*n)
    # n==0 is 1
    else:
        return 1

# taking number from user
num=int(input("Enter the number :"))

# if number is negative then error is generated
if (num<0):
    print("ERROR!!! Factorial does not exist for negative numbers.")

# it calls for the function if number is natural
else:
    print(f"The Factorial of {num} is {factorial(num)}")