#tuples 
coordinates = (4, 5)
person = ("John", 30, "Engineer")
single_item_tuple = (42,)  # Note the comma for a single-item tuple
tasks = ("task1", "task2", "task3")
countrys = ("USA", "Canada", "Mexico")


#Tuple operations   
print(coordinates[0])  # Accessing elements
print(len(person))  # Length of the tuple
print("Engineer" in person)  # Membership test
print(person + ("USA",))  # Concatenation
print(tasks * 2)  # Repetition
print(len(countrys))  # Length of the tuple
print("Canada" in countrys)  # Membership test