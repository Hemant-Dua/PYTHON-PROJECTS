This is a Python program to find the factorial of a number.

The program takes a number from the user and then uses a recursive function to calculate the factorial. If the number is negative, an error message is displayed. Otherwise, the factorial is printed to the console.

Here is the code for the program:

```python
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
```

The `factorial()` function takes a number as its input and then uses a recursive function to calculate the factorial. The recursive function works by calling itself with the input number decreased by 1 and then multiplying the result by the input number. This process continues until the input number is 0, at which point the function returns 1.

The `main()` function of the program takes a number from the user and then uses the `factorial()` function to calculate the factorial. If the number is negative, an error message is displayed. Otherwise, the factorial is printed to the console.