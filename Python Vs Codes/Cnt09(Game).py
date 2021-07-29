import random

# def func():
# print("Its Computer's Turn....")    #from this put in a different function
# random_number = random.randint(1, 3)
# if random_number == 1:
#     comp = 's'
# elif random_number == 2:
#     comp = 'w'
# else:
#     comp = 'g'
# print("Computer's Turn: ",comp)

# Made an function for taking the winner


def win_decision(n1, n2):
    if comp == 's' and you == 'w':
        return comp
    elif comp == 's' and you == 'g':
        return you
    elif comp == 'w' and you == 's':
        return you
    elif comp == 'w' and you == 'g':
        return comp
    elif comp == 'g' and you == 's':
        return comp
    elif comp == 'g' and you == 'w':
        return you
    elif comp == 's' and you == 's':
        both = 0
        return both
    elif comp == 'w' and you == 'w':
        both = 0
        return both
    else:
        both = 0
        return both


# print(comp)
# you=input("Your Turn...")
# a = win_decision(comp,you)
compscore = 0
playerscore = 0
for i in range(3):

    print(f"*****Roound {i+1}********")

    # Taking Computers random input
    print("Its Computer's Turn....")  # from this put in a different function
    random_number = random.randint(1, 3)
    if random_number == 1:
        comp = 's'
    elif random_number == 2:
        comp = 'w'
    else:
        comp = 'g'
    print("Computer's Turn: ", comp)  # to this in different function

    you = input("Your Turn: ")
    a = win_decision(comp, you)

    # pointing the score
    if a == comp:
        compscore = compscore+1
        print("The winner is Computer....\n\n")
    elif a == you:
        playerscore = playerscore+1
        print("You Won.....\n\n")
    else:
        playerscore = playerscore+0
        compscore = compscore+0
        print("Its Draw.....\n\n")

print(
    f"The Computer Score is: {compscore} \t And Player Score is : {playerscore}\n\n")

if compscore>playerscore:
    print("Computer had WON the match.... and score is ",compscore)
elif compscore < playerscore:
    print("Player had WON the match.... and score is ",playerscore)
else:
    print("Its a DRAW.....")