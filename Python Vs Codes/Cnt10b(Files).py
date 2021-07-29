# # Code for searching a word in a text file
# with open('Cnt10b.txt','r') as f2:
#     f=f2.read()
# if "Alisha" in f:
#     n="Alisha"
#     print("We got the word: ",n)
# else:
#     print("Word is not present.")

# for storig the high score of game
def game():
    return 112

new_score=game()
with open("Cnt10b.txt") as f:
    highscore= int(f.read())

if highscore<new_score:
    with open("Cnt10b.txt","w") as f:
        f.write(str(new_score))
else:
    print("Your score is low...")