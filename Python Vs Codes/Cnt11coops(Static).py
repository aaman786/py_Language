class Employee:
    company="Google"
    salary=19030

    def getsalary(self, signature):
        print(f"The company is {self.company} and salary {self.salary} \n {signature}")
    
    @staticmethod
    def greet():
        print("Good Morning Sir...")

e = Employee()
e.getsalary("Thanks!!")     #I added here by declaring signature above

e2 = Employee()
e2.company = "You Tube"
e2.salary = "10k"
e2.getsalary("Have a nice Day!!")   #I added here by declaring signature above
e2.greet()

