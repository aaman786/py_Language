fruits = ["Banana", "Watermelon", "Grapes", "Mango", "Pappya"]

print("By Using while Loop")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i+1

print("\n\nBy Using For Loop")
for items in fruits:
    print(items)

# Range in for
print("\n\nUsing the range in for Loop")
for i in range(8):  # it will write upto 7
    print(i)

print("\n\nWe can also use as.....")
for i in range(3, 6):  # it will print 3 to 5
    print(i)

print("\n\nWe can also use Range as.....")
for i in range(2, 8, 2):  # it will go to 8 but skips every 2nd value
    print(i)

# using else statement with for
print("\n\n Using Else with for")
for i in range(5):
    print(i)
else:
    print("The Loops gets over...")
