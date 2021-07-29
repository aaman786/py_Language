class Employee:
    company= "Google"
    def getsalary(self):    #self used for takling both class attribute as well as instance attribute
        print(f"The Company: {self.company} \tand Salary is: {self.salary}")

e = Employee()
print(e.company)
e.salary=5333400
e.getsalary()

#for 2nd Employee
e2 = Employee()
e2.company= "You Tube"
print(e2.company)
e2.salary="54769k"
e2.getsalary()

