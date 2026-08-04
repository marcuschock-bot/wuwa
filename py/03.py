name = str(input("Enter your name: "))
height = float(input("Enter your height in meters: ")) #Convert to float    

#Input validation
while True:
    try:    
        age = int(input("Enter your age: ")) #Convert to integer
        if 0 < age < 120:
            break
        else:
            print("Age must be a positive number. Please try again.")
    except ValueError:
            print("Invalid input. Please enter a valid age.")

#Output validation  
print(f"Hello {name}, you are {age} years old and {height} meters tall.")

#Exercise 1 (Create a simple calculator that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation. Handle invalid inputs gracefully.)
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
    
