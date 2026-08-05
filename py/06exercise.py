#CREATE A GROCERY LIST AND PERFORM VARIOUS OPERATIONS ON IT
#grocery_list = ["apples", "bananas", "milk", "bread"]       
##Accessing Elements
#print(grocery_list[0])  # Output: apples
#print(grocery_list[-1])  # Output: bread
#print(grocery_list[1:3])  # Output: ['bananas', 'milk']
#print(grocery_list[:2])  # Output: ['apples', 'bananas']

#grocery_list.append("eggs")  # Add to end
#grocery_list.insert(2, "cheese")  # Insert at index 2
#grocery_list.remove("milk")  # Remove by value
#popped_item = grocery_list.pop()  # Remove and return last item
#grocery_list.sort()  # Sort in place
#grocery_list.reverse()  # Reverse in place

#list operations    
#len(grocery_list)   
##"broccoli" in grocery_list  # Membership test
#grocery_list + ["oranges", "grapes"]  # Concatenation
#grocery_list * 2  # Repetition

#print(len(grocery_list))  # Output: Length of the list

#Exercise 2: Write a program that finds the largest and smallest number in list
numbers = [5, 2, 9, 1, 7, 6]
largest = max(numbers)
smallest = min(numbers)
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
for num in numbers:
    if num == largest:
        print(f"{num} is the largest number.")
    elif num == smallest:
        print(f"{num} is the smallest number.")
    else:
        print(f"{num} is neither the largest nor the smallest number.") 
