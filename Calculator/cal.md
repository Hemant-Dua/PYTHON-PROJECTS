This is a simple calculator program that can perform addition, subtraction, multiplication, and division.

To use the program, first enter the two numbers you want to calculate with. Then, enter the operation you want to perform. The program will then output the result of the calculation.

Here is an example of how to use the program:

```python
Enter the First Number: 10
Enter the Second Number: 5
Enter an operation: +
10 + 5 = 15
```

The program is written in Python. The following code snippet shows how to perform addition:

```python
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
print(f"{num1} + {num2} = {num1 + num2}")
```

The first line of code uses the `int()` function to convert the input from a string to an integer. The second line of code uses the `input()` function to get the input from the user. The third line of code uses the `f` string formatting function to print the result of the addition.

The other operations are performed in a similar way.