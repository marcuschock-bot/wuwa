fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, 3.14, True]
empty_list = []

#Accessing Elements
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: orange
print(numbers[1:4])  # Output: [2, 3, 4]
print(numbers[:3])  # Output: [1, 2, 3]
print(numbers[2:])  # Output: [3, 4, 5]

fruits.append("grape") #Add to end  
fruits.insert(1, "kiwi") #insert at index 1
fruits.remove("banana") #remove by value
popped = fruits.pop #remove and return last item
fruits.sort()       #sort in place
fruits.reverse() #remove in place   

# list operations
len(fruits)  # Length
"apple" in fruits  # Membership test
fruits + ["pear", "mango"]  # Concatenation 
fruits * 2  # Repetition

print(len(fruits))  # Output: Length of the list