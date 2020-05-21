import random
score=0
for i in range(0,100000):
    print("Guess Number between 0 to 9: ")
    num=int(input())
    r=random.randint(0,9)
    if(num==r):
        score+=1
        print("Noice!!!\nYour Score is ",score)
    else:
        print("You dissapointed!!!\nYour Score is ",score)
    print("try again")
