
myDict = {  # we can also chnge he name myDict
    "Fast": "In a Quick manner",
    "Name": "Shaalam",
    "marks": (4, 5, 6),  # list
    "anotherDict": {'Nick Name': 'Aamaan'},
    1: 2
}

print(myDict['Fast'])
print(myDict['Name'])
print("Before changing the Values: ", myDict['marks'])

changed = myDict['marks'] = [1, 0]  # changing the Values
print("Values are Changed: ", changed)  # printing the changed values

myDict['marks'] = [9, 7, 8]  # another way of chaning
print("Values are Changed Again: ", myDict['marks'])
print(myDict['anotherDict']['Nick Name'])


print("\n\nUsing the Dictionary Methos")
# printing the key list in dictionary
print("This Dictionary containing keys are: ",myDict.keys())

# knowing the type 
print("The Type is: ",type(myDict.keys()))
print("The Conversion into list: ",list(myDict.keys()))  #converting into the list

print("The values present inside the Dictioary are: ",myDict.values())
print("The Conversion into list: ",list(myDict.values()))  #converting into the list

# values and keys printing in an handy way in the form of tuples
print("Displaying both the keys as well as Values: ",myDict.items())

print("\n\nThe updation of the Dictionary....")
# updating Dictionary
print("The Dictionary before updaing: ",myDict)
myDict2 = {
    "Name2": "xyz"
}
myDict.update(myDict2)  #it will give this value to the myDict and update it
print("The Dictionary After updation: ",myDict) #This will be our updated dictionary

print("\n\nDifference between the two value callinng function")
#difference between calling a wethod in an dictionary
print("The value by .get function: ",myDict.get("Name"))
print("The value by Square Bracket function: ",myDict["Name"])
#here you think that both are same but they are not 

#here I am giving an key which not present in the Dictionary then
print("The value by .get function: ",myDict.get("Name0"))  #It will give the none
#print(myDict["Name0"])  #while it will throw an error



