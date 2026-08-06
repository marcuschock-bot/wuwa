#Write a function that checks if a number is prime or not
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#     print(f"{num} is a prime number.")

# num = int(input("Enter a number to check if it's prime: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

#Build a temperature converter that converts C elsius to Fahrenheit and vice versa
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temp = input("Enter temperature(Must add C symbol at the back) : ")
if temp[-1].upper() == "C":
    celsius = float(temp[:-1])
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")

