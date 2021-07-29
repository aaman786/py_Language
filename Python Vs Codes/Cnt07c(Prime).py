# This programm can only say that given number is prime or not
print("programm can only say that given number is prime or not")
num = int(input("Enter a number: "))
prime = True

for i in range(1, num):
    if(num % i == 0):
        print("This is not a prime number...  ")
        break
else:
    print("This is a Prime number...")

# This programm can print prime number upto given digit
print("\n\nThis programm can print prime number upto given digit")
num = int(input("Enter a number: "))
for i in range(1, num):
    for j in range(2, i):
        if(i % j == 0):
            break

    else:
        print(i)
