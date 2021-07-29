class Employee:
    work = "Operator"

    def work_details(self):
        print("My Work is:~ ",e.work)
        print("The work is hard but salary is good...")

class teacher(Employee):
    work= "Teaching"


    def work_details(self):
        super().work_details()
        print("\n")
        print("My Work is:~ ",t.work)
        print("The work is good but salary is low...")

class Programmer(teacher):
    work="Computer programming"

    def work_details(self):
        super().work_details()
        print("\n")
        print("My Work is:~",p.work)
        print("The work is best and salary is also good...")


e = Employee()
t= teacher()

p = Programmer()
p.work_details()
