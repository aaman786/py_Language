# This is an Tuple but it is simlar like list but the major differece is you can't change the tuple at any cost.
t = (3, 45, 7, 4, 1, 0)
print("The type you can see: ",type(t))
print("\n\nPrinting the tuple t: ", t)

t1 = ()  # This is an Empty Tuple
print("\n\nPrinting the tuple t1: ", t1)

t2 = (2,)  # The way of declaring tuple with single elements
print("\n\nThe tuple with single element t2: ", t2)

t = (1, 2, 4, 6, 8, 2, 10)  # REWRITTED the above tuple
print("\n\nThe tule t is: ", t)
# for counting the repeatatin of value in the tuple
print("The value repeating how much times: ", t.count(2))
print("The index is: ", t.index(2))  # for finding the value at which index

t4 = [4, 0, 5, 9, 0, 7, 0]
print("\n\nThe tuple is: ", t4)
# difference beween count and index function at tuple so here index will give starting index only
print("Number of zeroes by count function: ", t4.count(0))
print("Number of Zeroes by Index function: ", t4.index(0))
