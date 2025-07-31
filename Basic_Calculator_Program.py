# asking the user to input 2 num and operands 
a= float(input('Enter your first number:'))
b= float(input('Enter your second number:'))
operation_type = input('Enter the operation you want to perform (+, -, *, /): ')
# Check which operation the user wants and do it
if operation_type == '+':
    print('The result is:', a + b)
elif operation_type == '-':
    print('The result is:', a - b)
elif operation_type == '*':
    print('The result is:', a * b)
elif operation_type == '/':
    print('The result is:', a / b)
else:
    print('Invalid operation. Please enter +, -, *, or /.')