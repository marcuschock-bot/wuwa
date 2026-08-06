# #dictionaries
# student = {
#     "name": "Alice",
#     "age": 20,
#     "grades": "A",
#     "courses": ["Math", "Science", "English"]

# }
# #Accessing and modifying    
# print(student["name"])  # Accessing value by key
# print(student.get("age"))  # Accessing value using get()
# student["age"] = 21  # Modifying value
# student["email"]= "alice@example.com"

# #dictionaries method
# keys = student.keys()  # Get all keys
# values = student.values()  # Get all values
# items = student.items()  # Get all key-value pairs

# #Iterating through dictionary
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}: {value}")

# #Nested dictionaries
# company = {
#     "employees": {
#         "Alice": {"age": 30, "position": "Engineer"},
#         "Bob": {"age": 25, "position": "Designer"},
#         "positions": ["Engineer", "Designer", "Manager"]

# }
# }

# print (company["employees"].items())  # Accessing nested dictionary
# print(company["positions"])  # Accessing list within nested dictionary

#Exercise: Create a dictionary called student_records  with following information: "student_001"
# Simple student_records exercise
student_records = {
    "student_001": {"name": "John", "age": 19, "major": "Computer Science", "grades": [85, 92, 78]},
    "student_002": {"name": "Sarah", "age": 20, "major": "Biology", "grades": [90, 88, 95]},
}

# 2) Add student_003
student_records["student_003"] = {"name": "Mike", "age": 18, "major": "Math", "grades": [82, 79, 91]}

# 3) Update John's age to 20
student_records["student_001"]["age"] = 20

# 4) Loop and print each student's information simply
for sid, info in student_records.items():
    print(f"Student ID: {sid}, Name: {info['name']}, Major: {info['major']}")

