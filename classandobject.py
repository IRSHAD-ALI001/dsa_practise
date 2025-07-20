# from abc import ABC, abstractmethod

# # Abstraction
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# # Encapsulation
# class Animal:
#     def __init__(self, name):
#         self.__name = name  # Private attribute
#     def get_name(self):
#         return self.__name
#     def speak(self):
#         pass

# # Inheritance and Polymorphism
# class Dog(Animal):
#     def speak(self):
#         return f"{self.get_name()} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.get_name()} says Meow!"

# # Example usage
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())  # Buddy says Woof!
# print(cat.speak())  # Whiskers says Meow!



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}, {self.age} years old"

# person = Person("Alice", 25)
# print(person)        # Output: Alice, 25 years old
# print(str(person))   # Output: Alice, 25 years old



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"

# person = Person("Alice", 25)
# print(repr(person))  # Output: Person(name='Alice', age=25)
# print(person)        # Output: Person(name='Alice', age=25) (falls back to __repr__ if __str__ not defined)





# import unittest

# def add(a, b):
#     return a + b

# class TestMathOperations(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(0, 0), 0)

#     def test_add_invalid(self):
#         with self.assertRaises(TypeError):
#             add("2", 3)  # Should raise TypeError

# if __name__ == "__main__":
#     unittest.main()