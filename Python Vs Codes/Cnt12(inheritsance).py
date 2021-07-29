# Simple Inheritance
class Employee:
    name1 = "Arman"
    salary1 = "45k"


class programmer(Employee):

    def __init__(self, name2, salary2, language2):
        self.name2 = name2
        self.salary2 = salary2
        self.language2 = language2

    def display(self):
        print(f"The name is: {self.name2}")
        print(f"The salary is: {self.salary2}")
        print(f"The language is: {self.language2}")


# simple use of base class
print("The Employee's Details...")
e = Employee()
print(e.name1)
print(e.salary1)

# cinstructor use in derived class
print("\n\nThe Progammers Details...")
p = programmer("Aamaan", "40k", "python")
p.display()

# derived class use
print("\n\nDetails of Employee class by Derived class....")
print(p.name1)
print(p.salary1)
