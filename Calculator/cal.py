ques = input("Enter the Equation: ")

splited_ques = ques.split()

num1 = int(splited_ques[0])
num2 = int(splited_ques[2])
opr = splited_ques[1]

if opr=="+":
    print(f"{num1} + {num2} = {num1+num2}")
elif opr=="-":
    print(f"{num1} - {num2} = {num1-num2}")
elif opr=="*":
    print(f"{num1} * {num2} = {num1*num2}")
elif opr=="/":
    print(f"{num1} / {num2} = {num1/num2}")
else:
    raise ValueError("Invalid Inputs!!!")
