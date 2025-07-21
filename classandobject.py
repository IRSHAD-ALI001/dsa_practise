
# Abstraction Example: Coffee Machine System
# Abstraction hides implementation details and enforces a contract via abstract methods

from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    @abstractmethod
    def brew_coffee(self):
        # Abstract method to be implemented by subclasses
        pass
    
    @abstractmethod
    def clean_machine(self):
        # Abstract method to be implemented by subclasses
        pass

class EspressoMachine(CoffeeMachine):
    def brew_coffee(self):
        return "Brewing a strong espresso with high pressure"
    
    def clean_machine(self):
        return "Cleaning espresso machine: flushing water through system"

class CappuccinoMachine(CoffeeMachine):
    def brew_coffee(self):
        return "Brewing cappuccino with steamed milk foam"
    
    def clean_machine(self):
        return "Cleaning cappuccino machine: rinsing milk frother"

# Example usage
def main():
    espresso = EspressoMachine()
    cappuccino = CappuccinoMachine()
    
    print(espresso.brew_coffee())
    print(espresso.clean_machine())
    print(cappuccino.brew_coffee())
    print(cappuccino.clean_machine())
    
    # Cannot instantiate abstract class
    # machine = CoffeeMachine()  # TypeError

if __name__ == "__main__":
    main()







# Polymorphism Example: Payment Processing System
# Polymorphism allows different classes to implement the same method differently

class PaymentMethod:
    def process_payment(self, amount):
        # Base method to be overridden
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder
    
    # Override process_payment
    def process_payment(self, amount):
        return f"Processed ${amount} payment via Credit Card ending in {self.card_number[-4:]} for {self.card_holder}"

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    
    # Override process_payment
    def process_payment(self, amount):
        return f"Processed ${amount} payment via PayPal account {self.email}"

# Function to demonstrate polymorphism
def make_payment(payment_method, amount):
    print(payment_method.process_payment(amount))

# Example usage
def main():
    credit_card = CreditCard("1234567890123456", "John Doe")
    paypal = PayPal("john.doe@example.com")
    
    # Polymorphic behavior: same method, different implementations
    make_payment(credit_card, 100)
    make_payment(paypal, 50)

if __name__ == "__main__":
    main()








# Inheritance Example: Vehicle Rental System
# Inheritance allows child classes (Car, Bike) to inherit from a parent class (Vehicle)

class Vehicle:
    def __init__(self, brand, model, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_rented = False
    
    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            return f"{self.brand} {self.model} has been rented."
        return "Vehicle already rented."
    
    def return_vehicle(self):
        if self.is_rented:
            self.is_rented = False
            return f"{self.brand} {self.model} has been returned."
        return "Vehicle was not rented."
    
    def get_details(self):
        return f"{self.brand} {self.model}, ${self.rental_price_per_day}/day"

# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, num_seats):
        super().__init__(brand, model, rental_price_per_day)
        self.num_seats = num_seats
    
    # Extend parent method
    def get_details(self):
        return f"Car: {super().get_details()}, {self.num_seats} seats"

# Bike class inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, has_helmet):
        super().__init__(brand, model, rental_price_per_day)
        self.has_helmet = has_helmet
    
    # Extend parent method
    def get_details(self):
        helmet_status = "with helmet" if self.has_helmet else "without helmet"
        return f"Bike: {super().get_details()}, {helmet_status}"

# Example usage
def main():
    car = Car("Toyota", "Camry", 50, 5)
    bike = Bike("Honda", "CBR", 20, True)
    print(car.get_details())
    print(bike.get_details())
    print(car.rent())
    print(bike.rent())
    print(car.return_vehicle())
    print(bike.return_vehicle())

if __name__ == "__main__":
    main()








# Encapsulation Example: Bank Account System
# Encapsulation hides data (private attributes) and exposes only necessary methods

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        # Private attributes (using double underscore)
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = initial_balance
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Invalid or insufficient funds"
    
    # Getter method to access private balance
    def get_balance(self):
        return f"Balance for {self.__account_holder}: ${self.__balance}"
    
    # Getter method for account details
    def get_account_info(self):
        return f"Account Holder: {self.__account_holder}, Account Number: {self.__account_number}"

# Example usage
def main():
    account = BankAccount("John Doe", "1234567890", 1000)
    print(account.get_account_info())
    print(account.get_balance())
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.get_balance())
    # Trying to access private attribute directly will fail
    # print(account.__balance)  # AttributeError

if __name__ == "__main__":
    main()






# Library Management System demonstrating OOP concepts

from abc import ABC, abstractmethod
import datetime

# Abstraction: Abstract base class for library items
class LibraryItem(ABC):
    @abstractmethod
    def get_details(self):
        pass
    
    @abstractmethod
    def calculate_fine(self, days_overdue):
        pass

# Encapsulation: Book class with private attributes and public methods
class Book(LibraryItem):
    def __init__(self, title, author, isbn, copies_available):
        self.__title = title  # Private attribute
        self.__author = author
        self.__isbn = isbn
        self.__copies_available = copies_available
        self.__borrowed_by = None
        self.__due_date = None
    
    # Getter methods (Encapsulation)
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_copies_available(self):
        return self.__copies_available
    
    # Methods for borrowing and returning
    def borrow_book(self, member_id):
        if self.__copies_available > 0:
            self.__copies_available -= 1
            self.__borrowed_by = member_id
            self.__due_date = datetime.datetime.now() + datetime.timedelta(days=14)
            return True
        return False
    
    def return_book(self):
        if self.__borrowed_by:
            self.__copies_available += 1
            self.__borrowed_by = None
            self.__due_date = None
            return True
        return False
    
    # Implementing abstract method (Polymorphism)
    def get_details(self):
        return f"Book: {self.__title} by {self.__author} (ISBN: {self.__isbn}, Copies: {self.__copies_available})"
    
    def calculate_fine(self, days_overdue):
        fine_per_day = 1.0  # $1 per day
        return days_overdue * fine_per_day

# Inheritance: Magazine class inherits from LibraryItem
class Magazine(LibraryItem):
    def __init__(self, title, issue_number, publisher):
        self.__title = title
        self.__issue_number = issue_number
        self.__publisher = publisher
        self.__is_borrowed = False
    
    def borrow_magazine(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False
    
    def return_magazine(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False
    
    # Overriding abstract method (Polymorphism)
    def get_details(self):
        status = "Borrowed" if self.__is_borrowed else "Available"
        return f"Magazine: {self.__title}, Issue {self.__issue_number}, Publisher: {self.__publisher} ({status})"
    
    def calculate_fine(self, days_overdue):
        fine_per_day = 0.5  # $0.5 per day for magazines
        return days_overdue * fine_per_day

# Encapsulation: LibraryMember class
class LibraryMember:
    def __init__(self, member_id, name, email):
        self.__member_id = member_id
        self.__name = name
        self.__email = email
        self.__borrowed_items = []
    
    def get_member_info(self):
        return f"Member: {self.__name} (ID: {self.__member_id}, Email: {self.__email})"
    
    def borrow_item(self, item):
        if isinstance(item, Book):
            if item.borrow_book(self.__member_id):
                self.__borrowed_items.append(item)
                return f"{self.__name} borrowed {item.get_details()}"
        elif isinstance(item, Magazine):
            if item.borrow_magazine():
                self.__borrowed_items.append(item)
                return f"{self.__name} borrowed {item.get_details()}"
        return "Unable to borrow item"
    
    def return_item(self, item):
        if item in self.__borrowed_items:
            if isinstance(item, Book):
                item.return_book()
            elif isinstance(item, Magazine):
                item.return_magazine()
            self.__borrowed_items.remove(item)
            return f"{self.__name} returned {item.get_details()}"
        return "Item not borrowed by this member"

# Library class to manage the system
class Library:
    def __init__(self):
        self.__items = []
        self.__members = []
    
    def add_item(self, item):
        self.__items.append(item)
    
    def add_member(self, member):
        self.__members.append(member)
    
    def display_inventory(self):
        return "\n".join(item.get_details() for item in self.__items)
    
    def display_members(self):
        return "\n".join(member.get_member_info() for member in self.__members)

# Example usage
def main():
    # Create library
    library = Library()
    
    # Create items
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 3)
    book2 = Book("1984", "George Orwell", "978-0451524935", 2)
    magazine1 = Magazine("National Geographic", "2025-07", "NatGeo")
    
    # Add items to library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)
    
    # Create members
    member1 = LibraryMember("M001", "John Doe", "john@example.com")
    member2 = LibraryMember("M002", "Jane Smith", "jane@example.com")
    
    # Add members to library
    library.add_member(member1)
    library.add_member(member2)
    
    # Demonstrate functionality
    print("Library Inventory:")
    print(library.display_inventory())
    print("\nLibrary Members:")
    print(library.display_members())
    
    # Borrowing and returning
    print("\n" + member1.borrow_item(book1))
    print(member2.borrow_item(magazine1))
    print("\nUpdated Inventory:")
    print(library.display_inventory())
    
    # Calculate fine (example)
    print(f"\nFine for book1 (5 days overdue): ${book1.calculate_fine(5)}")
    print(f"Fine for magazine1 (5 days overdue): ${magazine1.calculate_fine(5)}")
    
    # Return items
    print("\n" + member1.return_item(book1))
    print(member2.return_item(magazine1))
    print("\nFinal Inventory:")
    print(library.display_inventory())

if __name__ == "__main__":
    main()