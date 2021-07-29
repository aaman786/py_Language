# ses are collection of nonrepeatative elements
set1 = {2, 1, 4, 6, 8, 1}
print("For proof printing the type: ", type(set1))
print("The set is ", set1)  # it will not print the repatative elements

# creating an Empty set
print("\n\nAbout the Empty sets....")
s1 = {}  # This will create an Empty Dictionary but not a set
print("The type is: ", type(s1))  # This will igve a proof of type
s2 = set()  # This will give me an Enpty set
print("The type is: ", type(s2))  # This will give the proof of type

# Methods for set
# For adding value in set
print("\n\nAdding the values at Empty Set...")
s2.add(5)  # it will not be accepted by the set as it is already signed at line 19
s2.add(4)
s2.add(4)  # it will not be accepted by the set as it is already signed above
s2.add(5)
print("THe set will get the provided values: ", s2)

# here if i want to add list and tuple
print("\n\nAdding List and Tuple....")
# s2.add([3,4,5])  #it will through an error because list can be change so it not accepted by set
# s2.add({2:3}) #it will ot accept dictionary also.
s2.add((3, 4, 2, 1))  # Adding of Tuple
print("I can also an Tuple but not the list(as it is changable) and dictionary: ", s2)

# method for obtaining the length of set
print("\n\nMethod for the length of set.....")
print("Our set is s2 = ", s2)
print("The length of the set is: ", len(s2))

# method for reoving an elements
print("\n\nMethod for removing the set Elements.....")
print("Our set s2 = ", s2)
s2.remove(4)    #this will only remove the present values in the set otherwise thee wouls be an eror
print("We are removing 4 then set would like: ", s2)



