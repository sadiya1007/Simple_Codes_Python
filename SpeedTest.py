import time
original=("A rat can fall from a five story building without injury")
orig=list(original.split(" "))
print("Welcome to Speed Test.\nThe Details are:\n1)Enter the line displayed and press Enter\n2)Mind Punctuations\nEress Enter To Start")
a=input()
starttime=time.time()
print("A rat can fall from a five story building without injury")
entered=list(input().split(' '))
endtime=time.time()
score=0
for i in range(len(entered)):
    if(entered[i]==orig[i]):
          score+=1
print("\n\nResults are\n  Words Entered correctly",score,"\n  Total words is 11")
print("  Time taken",round(endtime-starttime,3),"seconds")
print("  Accuracy is",round((score/11)*100,2),"%")
