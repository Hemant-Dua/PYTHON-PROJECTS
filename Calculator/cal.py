num1=int(input("Enter the First Number :"))
num2=int(input("Enter the Second Number :"))
print("Enter an operation :")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

opr = input()

if opr=="+":
    print(f"{num1}+{num2}={num1+num2}")
    
elif opr=="-":
    print(f"{num1}-{num2}={num1-num2}")

elif opr=="*":
    print(f"{num1}*{num2}={num1*num2}")

elif opr=="/":
    print(f"{num1}/{num2}={num1/num2}")

else:
    print("Try Again...")