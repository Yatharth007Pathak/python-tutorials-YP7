'''
Encapsulation bundles the attributes (data) and the methods (functions) together in one entity - class

Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit or class. 
It also involves restricting direct access to some of the object's components, which is called data hiding.
Encapsulation is the mechanism of hiding the internal state of an object and only exposing a controlled interface. 
In Python, this is typically done using private attributes and methods.
'''

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner                                          # Initialize the account with an owner and a balance
        self.__balance = balance                                    # Private attribute for the balance

    def deposit(self, amount):
        self.__balance += amount                                    # Add the specified amount to the balance
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:                                # Withdraw the specified amount if sufficient balance is available
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance                                       # Return the current balance

acc = Account("Alice", 1000)                                        # Create an instance of Account
# Perform deposit and withdrawal operations
acc.deposit(500)             # Output: Deposited: 500
acc.withdraw(300)            # Output: Withdrawn: 300
print(acc.get_balance())     # Output: 1200                         # Print the current balance


'''
Let's break down the code to understand the Account class, 
which encapsulates the concept of a bank account with private attributes and methods for depositing, withdrawing, and checking the balance:

class Account:
This defines a class named Account, which models a bank account with basic functionality for managing money.

def __init__(self, owner, balance=0):
This is the constructor method for the Account class. It initializes a new instance of Account.

self.owner = owner
This line sets the owner attribute of the account to the value provided when the account is created. 
It represents the person who owns the account.

self.__balance = balance
This line initializes the __balance attribute to the value provided (or 0 if no value is provided). 
The double underscore (__) makes this attribute private, meaning it cannot be accessed directly from outside the class.

def deposit(self, amount):
This method allows for depositing money into the account.

self.__balance += amount
This line adds the deposited amount to the private __balance attribute.

print(f"Deposited: {amount}")
This line prints a message indicating the amount deposited.

def withdraw(self, amount):
This method allows for withdrawing money from the account.

if amount <= self.__balance:
This line checks if the withdrawal amount is less than or equal to the current balance.

self.__balance -= amount
If the check passes, this line subtracts the withdrawn amount from the private __balance attribute.

print(f"Withdrawn: {amount}")
This line prints a message indicating the amount withdrawn.

else:
This part handles the case where the withdrawal amount exceeds the balance.

print("Insufficient balance")
This line prints a message indicating that there is not enough balance to complete the withdrawal.

def get_balance(self):
This method returns the current balance of the account.

return self.__balance
This line returns the private __balance attribute.

acc = Account("Alice", 1000)
This line creates an instance of the Account class with the owner set to "Alice" and an initial balance of 1000. 
This instance is assigned to the variable acc.

acc.deposit(500)
This line calls the deposit method on the acc instance to deposit 500 into the account.

acc.withdraw(300)
This line calls the withdraw method on the acc instance to withdraw 300 from the account.

print(acc.get_balance())
This line calls the get_balance method on the acc instance and prints the current balance of the account.

Summary:
Private Attribute: The __balance attribute is private and cannot be accessed directly from outside the class. This encapsulation helps protect the balance from unauthorized modifications.
Deposit and Withdraw Methods: These methods modify the balance based on transactions and print relevant messages.
Balance Check: The get_balance method provides a way to check the current balance without exposing the private __balance attribute directly.
Encapsulation: The code effectively uses encapsulation to control access to the balance and ensure that it is only modified through the provided methods.
'''