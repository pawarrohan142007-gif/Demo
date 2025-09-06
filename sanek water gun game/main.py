import random
'''
1 for sanke
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s,w,g): ")

if youstr not in ('s','w','g') :
    print('please enter the value from (s,w,g)')
    
youDict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "sanke", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"you chose{reversedict[you]}/ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you ==1):
         print("You Win")

    elif(computer ==-1 and you ==0):
        print("you lose!")

    elif(computer == 1 and you ==-1):
        print("You lose!")

    elif(computer ==1 and you ==0):
        print("you win")

    elif(computer == 0 and you ==-1):
        print("You Win")

    elif(computer ==0 and you ==1):
        print("you lose!")

    else:
        print("something went wrong")


