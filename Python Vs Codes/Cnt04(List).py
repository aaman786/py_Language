# Creating a list
a = [2, 4, 6, 8, 10]
print("The build list is: \n", a)

print("\nThe value at index zero: ", a[0])  # showing the value at the 0 index

# changing the value at 0 index
a[0] = 97
print("\nThe Changed Value is: ", a)
print("The value is: ", a[0])

# We can Create a list with differrent Types of Items
b = [4, "Tommy", "Apple", 77, 67.5]
print(b)
# This will give upto 4 index and this is slicing tha list
print("Now printing half or wanted Ones: ", b[0:4])

# sorting of List
print("\n\n")
a1 = [2, 7, 9, 3, 4]
a1.sort()  # for Arranging
print("Arranging in acending order: ", a1)
a1.reverse()
print("Reversing the Arranged list: ", a1)
a1.append(45)  # Append means adding the value at last
print("On adding an element at last by append function: ", a1)
a1.insert(3, 0.5)  # adding Value 00 at index 3
print("The addition of value at index 3: ", a1)
a1.pop(3)  # This will delet the value at index 3
print("The value at index 3 is removed: ", a1)
a1.remove(45)  # this will find the value 45 and remove it.
print("The value 45 is removed from the list: ", a1)
