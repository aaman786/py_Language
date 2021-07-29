# Function for calculation factorial by iterative approach
def factorial_iterative(n1):
    product=1
    for i in range(n1):
        product=product*(i+1)       
    return product

# By recursive approach
def recursion_factorial(n2):
    if n2==1 or n2==0:
        return 1
    return n2*recursion_factorial(n2-1)

n=int(input("Enter any number for factorial calculation: "))
f1=factorial_iterative(n)
print(f"This is the Answer by iterative approach:- {f1}")

f2=recursion_factorial(n)
print(f"This is the Answer by recursive approach:- {f2}")