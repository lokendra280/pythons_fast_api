# from datetime import date

# class Calculator:

#     def __init__(self, version):
#         self.version = version

#     def description(self):
#             print(f"This is a calculator of version {self.version}")

# calc1 = Calculator(10)
# calc2 = Calculator(20)

# calc1.description()
# calc2.description()


from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def age_from_year(cls, name, birth_year):
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)

macs = Person("Macs", 25)
macs.display()

# Creating a person using the class method
person2 = Person.age_from_year("Alice", 1990)
person2.display()
