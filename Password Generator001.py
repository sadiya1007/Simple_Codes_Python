import random
print("This is a password generator. \nPress Y for YES and N for NO.")
n=int(input("Enter length of password you want: "))
passwordstack=list()
password=''
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
locase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']

a=input("Digits ? " )
b=input("LowerCase Letters ?" )
c=input("UpperCase Letters ?" )
d=input("Symbols ?" )

if a=='Y' or a=='y':
    passwordstack+=digits
if b=='Y' or b=='y':
    passwordstack+=locase
if c=='Y' or c=='y':
    passwordstack+=upcase
if d=='Y' or d=='y':
    passwordstack+=symbols

for i in range(0,n):
    password+=random.choice(passwordstack)

print("Your Random Password is :  ",password)
