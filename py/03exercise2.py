#Exercise 2 (create a simple 3 quiz game that asks the user three questions and keeps track of their score. Provide feedback on whether their answers are correct or incorrect.)
score = 0

# Question 1
answer1 = input("What is the capital of France? ")
if answer1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")
   
# Question 2
answer2 = input("What is the largest planet in our solar system? ")
if answer2.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 3
answer3 = input("What is the chemical symbol for gold? ")
if answer3.lower() == "au":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")
    
print(f"Your final score is: {score}/3")