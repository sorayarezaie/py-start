num1 = int(input("Give me the first number "))
num2 =int(input("Give me the second number"))
operand = input("give me the operator")
result = 0;
if operand == '+':
    result = num1 + num2
elif operand == '-':
    result = num1 - num2
elif operand == '*':
    result = num1 * num2
elif operand == '/':
    if num1 != 0:
        result = num1 / num2
    else:
        print('It cannot be divided by zero')
else:
    print('Invalid Operator')
print("the result of your given numbers is: "+ result)