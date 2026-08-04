#weather = "sunny"   
#temperature = 75 

#if weather == "sunny" and temperature > 70:
 #   print("It's a great day for outdoor activities!")
#else:
  #  print("Maybe stay indoors today.")

#Exercise (create a simple program that categorizes BMI (Body Mass Index) based on user input for weight and height. Provide feedback on whether their BMI is underweight, normal weight, overweight, or obese.
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "normal weight"
elif 25 <= bmi < 29.9:
    category = "overweight"
else:
    category = "obese"

print(f"Your BMI is {bmi:.2f}. Category: {category}.")


