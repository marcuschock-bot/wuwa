# #Classes
# class Person:

#     species = "Homo sapiens"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."

#     def have_birthday(self):
#         self.age += 1
#         return f"Happy Birthday! I am now {self.age} years old."

# #object instantiation
# person1 = Person("Marcus", 19)
# person2 = Person("Sophia", 25)

# #Accessing attributes
# print(person1.name)  # Output: Marcus
# print(person2.age)   # Output: 25
# print(person1.greet())  # Output: Hello, my name is Marcus and I am 19 years old.
# print(person2.have_birthday())  # Output: Happy Birthday! I am now 26 years old.
# print(Person.species)

class BankAccount:
    def __init__(self, account_number, owner, balance = 0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}.New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw ${amount}")
            return f"Withdrew ${amount}.New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def transaction_history (self):
        return self.transaction_history

account = BankAccount("12345" , "Alice" , 1000000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
