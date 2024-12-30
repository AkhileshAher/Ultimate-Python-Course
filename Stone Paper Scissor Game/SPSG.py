import random

print("Welcome to STONE PAPER SCISSOR GAME")
print("REMEMBER : \n1 Stone \n2 Paper \n3 Scissor\nThe Stone Beats Scissor\nThe Paper beats Stone\n The Scissor Beats Paper")
score1=0
score2=0

while(True):
    list1=[1,2,3]
    computer = random.choice(list1)
    users=int(input("Enter your Choice : "))

    if(users==0 or users>3):
        raise ValueError("Enter Value from 1 , 2 and 3")
    
    if(computer==1):
        a="Stone"
    elif(computer==2):
        a="Paper" 
    else:
        a="Scissor"

    if(users==1):
        b="Stone"
    elif(users==2):
       b="Paper"
    else:
       b="Scissor"

    print(f" Battle {a} vs {b}")

    if(computer==2 and users==1) or (computer==1 and users==3) or (computer==3 and users==2):
        score1 =score1 + 1

    elif(computer==1 and users==2) or (computer==3 and users==1) or (computer==2 and users==3):
        score2=score2+1 

    else:
        score1=score1
        score2=score2
    
    print(f"------------Scores-----------\nComputer = {score1} \nUser = {score2}")
    
    if(score1==10 or score2==10):
        break

print("----GAME OVER------")

if(score1==10):
    print("Winner : Computer")
else:
    print("Winner : User")
