# person = ("Alice", "Bob", "Charlie")  # Tuple of names
# subject = ("Math", "Science", "English")  # Tuple of subjects
# grades = (85, 92, 78, 90, 88, 95)  # Tuple of grades

#Exercise 1: Create a system that stores student grades as tuples and uses sets to find unique subjects and students
# name = input("Enter student name: ")
# subject = input("Enter subject: ")
# grade = int(input("Enter grade: "))

# sets = set()
# sets.add(subject)
# print(sets)

grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95)
]
name = input("Enter student name: ")
subject = input("Enter subject: ")

found = False
for student, subj, score in grades:
    if student.lower() == name.lower() and subj.lower() == subject.lower():
        print(f"{student} has score {score} in {subj}")
        found = True
        break

if not found:
    print("No grade found for that student and subject.")

# name2 = set()
# subject2 = set()
# for name, subject, score in grades:
#     name2.add(name)
#     subject2.add(subject)
# print(f"Unique students: {name2}")
# print(f"Unique subjects: {subject2}")

# alices_grades = []
# for score in grades:
#     if score[0] == "Alice":
#         alices_grades.append(score[2])
# print(f"Alice's grades: {alices_grades}")
