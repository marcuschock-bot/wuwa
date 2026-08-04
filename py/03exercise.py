number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")    
while True:
    if operator == "+":
        result = number_1 + number_2
        break
    elif operator == "-":
        result = number_1 - number_2
        break
    elif operator == "*":
        result = number_1 * number_2
        break
    elif operator == "/":
        if number_2 != 0:
            result = number_1 / number_2
            break
        else:
            print("Error: Division by zero is not allowed.")
            operator = input("Enter a valid operator (+, -, *, /): ")
    else:
        print("Invalid operator. Please try again.")
        operator = input("Enter a valid operator (+, -, *, /): ")   
    