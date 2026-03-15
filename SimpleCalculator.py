num1 = float(input("enter your first number:"))
num2 = float(input("enter your second number:"))
x = str(input("enter '+','-','*','%'"))
if x == "+":
    print(num1 + num2)
elif x == "-":
    print(num1 - num2)
elif x == "*":
    print(num1 * num2)
elif x == "%":
    print(num1 + num2)
else:
    print("error")