import random

print("/********************************************************/\n")
print("                   Rock-Paper-Scissor                   \n")
print("/********************************************************/\n")


k = 0
comp_move = [" "," "," "," "," "]
user_move = [" "," "," "," "," "]
for i in range(5):
    rand_num = random.randint(1,3)
    if rand_num == 1:
        comp_move[k] = "Rock"
    elif rand_num == 2:
        comp_move[k] = "Paper"
    elif rand_num == 3:
        comp_move[k] = "Scissor"
    k = k + 1

scUser = 0
scComp = 0

print("---Welcome---\n")
k=0
for i in range(5):
    print("\nPlay\n")
    choice='a'
    while(choice!='y'):
        file = open("testfile.txt","r")
        move = file.readline()
        file.close()
        print("\nYour move => "+move)
        choice = input("\nPress Y if its correct : ")
        if choice=='y':
            user_move[k]=move
            print("\nPCs move => "+comp_move[k])
            print("\n"+user_move[k]+" Vs "+comp_move[k])
            if user_move[k]=="Scissor" and comp_move[k]=="Rock":
                scComp = scComp + 1
                print("\nYou lose")
            elif user_move[k]=="Scissor" and comp_move[k]=="Paper":
                scUser = scUser + 1
                print("\nYou win")
            elif user_move[k]=="Rock" and comp_move[k]=="Paper":
                scComp = scComp + 1
                print("\nYou lose")
            elif user_move[k]=="Rock" and comp_move[k]=="Scissor":
                scUser = scUser + 1
                print("\nYou win")
            elif user_move[k]=="Paper" and comp_move[k]=="Scissor":
                scComp = scComp + 1
                print("\nYou lose")
            elif user_move[k]=="Paper" and comp_move[k]=="Rock":
                scUser = scUser + 1
                print("\nYou win")
            k = k+1
            input()
k = 0
for i in range(5):
    print(user_move[k]+" Vs "+comp_move[k])
    k = k + 1


if scUser<scComp:
    print("Game over")
else:
    print("Congratulations!!")