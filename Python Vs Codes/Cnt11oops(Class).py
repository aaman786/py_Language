class Employee:
    name="Aman"     #This is class attributes
    employ_Id= 10    #This is class attributes
    salary= "10k"     #This is class attributes      

e = Employee()
print("1st Employee...")
print("Name is: ",e.name)
print("Id is: ",e.employ_Id)
print("The salary is: ",e.salary)

print("\n\n2nd Employee...")
e2 = Employee()
e2.name="Shameer"   #This is instance attribute, we can also declare here also
print(e2.name)
print(e2.salary)
