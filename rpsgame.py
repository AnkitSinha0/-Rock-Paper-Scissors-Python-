import random
user_score=0
comp_score=0
ties=0
print("welcome to game of rock paper scissors")
print('''Winning Rules
1.Rock vs Paper --> Paper
2.Paper vs Scissors -->Scissors
3.Scissors vs Rock -->Rock''')
print('''Choices:
1.Rock
2.Paper
3.Scissors''')
while True:
    print("Rock,Paper or Scissors?")
    
    user=int(input())
    while user>3 or user<1:
        user =int(input("Enter Valid Input"))
    if user == 1:
        user_choice = "Rock"
    elif user == 2:
        user_choice ="Paper"
    else:
        user_choice ="Scissors"
        print("user's choice is",user_choice)
    comp=random.randint(1,3)
    if comp==1:
        comp_choice = "Rock"
    elif comp==2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print("computer's choice is",comp_choice)
    if ((user_choice == "Paper" and comp_choice == "Rock")or(user_choice =="Rock" and comp_choice =="Paper")):
        print("Paper wins")
        result="Paper"
    elif ((user_choice == "Paper" and comp_choice == "Scissors")or(user_choice =="Scissors" and comp_choice =="Paper")):
        print("Scissors wins")
        result="Scissors"
    elif user_choice==comp_choice:
        print("Tie")
        result= "Tie"
    else:
        print("Rock wins")
        result="Rock"
    
    if result == "Tie":
        ties+=1
    elif result == user_choice:
        print("user won")
        user_score+=1
    else:
        comp_score+=1
        print("computer won")
    print("user score:",user_score)
    print("comp score:",comp_score)
    print("Ties:",ties)
    repeat=input("Do you want to play again?")
    if repeat == "no":
        print("Thanks for playing")
        break
    elif repeat == "yes":
        continue
    
