def maximum(n1, n2, n3):
    if n1 > n3:
        g1 = n1
    else:
        g1 = n3
    if g1 > n2:
        g = g1
    else:
        g = n2
    return g


num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))
f = maximum(num1, num2, num3)
print(f"The Greatest number of given three numbers is: {f}")

# Printing in one Line
print("How", end="")
print("are")
print("you?")
