# use of break statements in loop
print("\n\nUsing the Break statement in Loops.....")
for i in range(10):
    print(i)
    if i == 5:
        print("Got with 5 So breaking the Loop... ")
        break

# Use of Continue statements in Loops
print("\n\nUsing the Continue statement in Loops.....")
for i in range(10):
    if i == 5:
        print("value becomes 5,so it got skipped only..")
        continue
    print(i)

# using pass statements in Loops
print("\n\nUsing Pass statements....")
i = 4
if i > 0:
    print(i)
    pass  # meaning of pass is do nothing
print("The Pass statement is above.")
