#                                          classandobject.py
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

# Object
s1 = Student("Irshad", 101)
s1.display()






#                                          encapsulation.py
class ATM:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.__balance

# Object
my_atm = ATM(5000)
my_atm.deposit(1000)
my_atm.withdraw(2000)
print("Remaining Balance:", my_atm.get_balance())







#                                   abstraction.py
class WashingMachine:
    def __init__(self):
        pass

    def start(self):
        self.__fill_water()
        self.__add_detergent()
        self.__start_wash()

    def __fill_water(self):
        print("Filling water...")

    def __add_detergent(self):
        print("Adding detergent...")

    def __start_wash(self):
        print("Washing clothes...")

# User only calls:
wm = WashingMachine()
wm.start()





#                                          inhertance.py
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} vehicle is moving.")

class Car(Vehicle):  # Inheritance
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def play_music(self):
        print(f"Playing music in {self.model}.")

# Object
c = Car("Toyota", "Innova")
c.drive()
c.play_music()









#                                     polymorphism.py
class Shape:
    def draw(self):
        print("Drawing a shape.")

class Circle(Shape):
    def draw(self):  # Method overriding
        print("Drawing a circle.")

class Square(Shape):
    def draw(self):
        print("Drawing a square.")

# Objects
shapes = [Circle(), Square(), Shape()]
for s in shapes:
    s.draw()










#                 wholee oops
class Animal:
    # Class variable
    kingdom = "Animalia"

    def __init__(self, name, sound):
        self.name = name              # Public attribute
        self._mood = "happy"          # Protected attribute
        self.__sound = sound          # Private attribute

    # Encapsulation: Getter for private variable
    def get_sound(self):
        return self.__sound

    # Encapsulation: Setter for private variable
    def set_sound(self, sound):
        self.__sound = sound

    # Abstraction: Hiding complex logic
    def describe(self):
        print(f"{self.name} is feeling {self._mood} and says '{self.__sound}'.")

    # Static method
    @staticmethod
    def general_info():
        print("Animals are multicellular, eukaryotic organisms.")

    # Class method
    @classmethod
    def kingdom_info(cls):
        print(f"All animals belong to the {cls.kingdom} kingdom.")


# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "woof")
        self.breed = breed

    # Polymorphism - Method Overriding
    def describe(self):
        print(f"{self.name} is a {self.breed}, feeling {self._mood} and says '{self.get_sound()}'.")


# Polymorphism - Method Overloading simulation (using default args)
def make_sound(animal, times=1):
    for _ in range(times):
        print(animal.get_sound())


# Object creation
dog = Dog("Buddy", "Golden Retriever")

# Using methods
dog.describe()
dog.set_sound("bark!")
make_sound(dog, 3)

# Static & class method
Dog.general_info()
Dog.kingdom_info()











#####          whole oops with bank account example
class BankAccount:
    # Class variable (shared by all accounts)
    bank_name = "Happy Bank of Python"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Encapsulated (private)

    # Encapsulation: getter
    def get_balance(self):
        return self.__balance

    # Deposit method with abstraction
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Withdraw method with abstraction
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    # Abstraction + Polymorphism: will be overridden
    def display_details(self):
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ₹{self.__balance}")

    # Static method
    @staticmethod
    def bank_info():
        print("Welcome to the Happy Bank of Python. We value your happiness!")

    # Class method
    @classmethod
    def show_bank_name(cls):
        print(f"This account belongs to: {cls.bank_name}")


# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=5.0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    # Polymorphism - Overriding method
    def display_details(self):
        super().display_details()
        print(f"Interest Rate: {self.interest_rate}%")


# Creating real-world object
my_account = SavingsAccount("Irshad", 1000)

# Using OOP features
my_account.display_details()
my_account.deposit(500)
my_account.withdraw(200)
print("Balance accessed through getter:", my_account.get_balance())

# Static & class methods
SavingsAccount.bank_info()
SavingsAccount.show_bank_name()



















