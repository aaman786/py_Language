str1 = '''Are you Going'''
str2 = ''' to the Market.'''
str = str1 + str2  # adding the upper strings
print("The input string is:~~~  ", str)

# if here I want one char then I will look it throught index of string
print(str[0])
print(str[1])
print(str[2])
print(str[3])

# Another syntax for reading string throught index
print("\n\nThe another Syntax for ", str[0:6])

# Escape value
# it will skip every 2nd time value
print("\n\nThe Escape Value: ", str[0:10:2])

print("\n\nThe length of string: ", len(str))
print("Shows the last word if its same gives: ", str.endswith("Market"))
print("The Total numbers of a present in ", str.count("a"))
print("Capitalization of first letter: ", str.capitalize())
print("Finding the word: ", str.find("going"))
print(str.replace("Going to", ("gonna")))
