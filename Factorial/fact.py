# function for factorial

def factorial(n):
    if n!=0:
        return (factorial(n-1)*n)
    else:
        return 1

num=int(input("Enter the number: "))

if (num<0):
    print("ERROR!!! Factorial does not exist for negative numbers.")
else:
    print(f"The Factorial of {num} is {factorial(num)}")