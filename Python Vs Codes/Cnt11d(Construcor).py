# class Employee:
#     def __init__(self,company,salary,age):
#         self.company= company
#         self.salary= salary
#         self.age= age

#     def getdetails(self):
#         print(f"The name of Company is: {self.company}")
#         print(f"The salary is: {self.salary}")
#         print(f"The age is: {self.age}")

#     @staticmethod
#     def getdata():
#         print("In the name of god, who is merciful")

# print("Using the constructor....")
# e = Employee("Microsoft",53800,29)
# e.getdetails()


class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getdetails(self):
        print(f"Name is: {self.name} And marks is: {self.marks}")


s1 = student("Arman", 48)
s1.getdetails()

s2 = student("Aamaan", 21)
s2.getdetails()
