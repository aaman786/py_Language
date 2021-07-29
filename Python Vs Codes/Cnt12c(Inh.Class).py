class Employee:
    name = "Aaman"
    salary = "450k"

    # changing the Salary
    @classmethod
    def change_salary(cls, new_amt):
        print(f"changing the salary amount '{e.salary}' with '{new_amt}'")
        cls.salary = new_amt
    @classmethod
    def change_name(cls, new_name):
        print(f"changing the name '{e.name}' with '{new_name}'")
        cls.name = new_name


e = Employee()
#changing the salary
print("Previous salary: ", e.salary)
e.change_salary("200k")
print(f"The changed Salary is: {e.salary} ")

#changing the name
print("\n\n")
print("The prevoius name is: ", e.name)
e.change_name("Shaalam")
print("The changed name is: ", e.name)
