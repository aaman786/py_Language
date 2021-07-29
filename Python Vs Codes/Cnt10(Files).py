# reading the file
print("Reading the content of the file........")
f = open('Cnt10.txt', 'r')
# a= f.read() #for reeading th  whole content present in the file
a = f.readline()  # for reeading lines present in the file
print(a)
f.close()

# Using the write mode
print("/n/nWriting in the file by write Mode")
f = open('Cnt10.txt', 'w')  # it erase the cotent
f.write("Computer Contains various types of passive elements.")
f.close()

# using the appending mode
print("\n\nPerforming appending operation on the file")
f = open('Cnt10.txt', 'a')
f.write(".\nI am appending...")  # it will add the content at end
f.close()

# with statement for modes which automatically closes the file
with open('Cnt10.txt', 'r') as f:
    print("\n\nShowing the content present in the file with the help of r mode")
    a = f.read()
print(a)
with open('Cnt10.txt', 'a') as f:
    print("Addding the content in the file by the use of a mode")
    f.write("\nI am the one.")
with open('Cnt10.txt', 'r') as f:
    print("\n\nThe new content added in he file is")
    a = f.read()
    print(a)
