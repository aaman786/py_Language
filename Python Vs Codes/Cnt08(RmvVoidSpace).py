def creating_New(string, rmword):
    newstr = string.replace(rmword, "")
    return newstr.strip()   #for removing the blank space.


str1 = "     Shubham this is Sentence    "
n = creating_New(str1, "Shubham")
print("The new String is: ~~~",n)
