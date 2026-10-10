from mathutils import add, multiply, factorial, PI, Calculator  
result = add(5,3)
print(f"Addition result: {result}")

import os
import sys
import datetime
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Now date: {now}")
print(f"Today's Date: {today}")
print(f"Current Date and Time: {formatted_date}")

random_number = random.randint(1, 100)
random_choice = random.choice(['apple' , 'banana' , 'orange'])
numbers = [1,2,3,4,5]
random.shuffle(numbers)

print(f"Random Number: {random_number}")
print(f"Random Choice: {random_choice}")
print(f"Shuffled List: {numbers}")


