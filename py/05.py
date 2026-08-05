#for i in range(5): # 0,1,2,3,4  
 #   print(i)
#
#For i in range(1,6): #1,2,3,4,5
  #  print(i)

#for i in range(0 , 10, 2): # 0,2,4,6,8
 #   print(i)

#Exercise 1 Create a multiplication table generator 
#for i in range(1, 11):
 #   for j in range(1, 11):
  #      print(f"{i} x {j} = {i * j}")
   # print()  # Print a blank line after each table

#Exercise 2 Write a program that finds all the prime numbers up to a given number n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
n = int(input("Enter a number: "))
print(f"Prime numbers up to {n}:")

for num in range(2, n + 1):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

        