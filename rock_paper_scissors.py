
print("WELCOME TO MY GAME ROCK--PAPER--SCISSORS")
print("  ")


import random

def gamewin(comp, you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
    
while(True):
    print("Computer's turn:  rock{r} or paper{p} or scissors{s}")
    randno= random.randint(1, 3)
    if randno==1:
        comp='r'
    elif randno==2:
        comp='p'
    elif randno==3:
        comp='s'

    you= input("Your turn:  rock{r} or paper{p} or scissors{s}: --->> ")
    g=gamewin(comp, you)


    print(f"Computer chose {comp}")
    print(f"You chose {you}")


    if g==None:
        print("Game tie!")
    elif g:
        print("Game win!")
    else:
        print("Game lose!")

    print("Game by SUBHADIP DAS")
    print("----------------------------")