num1= int(input("Enter your number:"))
num2= int(input("Enter your number:"))

operator =  input("Enter your operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
elif operator == "%":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 % num2)
else:
    print("Please enter a valid operator +,-,*,/,%")
