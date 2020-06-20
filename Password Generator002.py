import random
print("This is a password generator. \nPress Y for YES and N for NO.")
n=int(input("Enter length of password you want: "))
passwordstack=list()
password=''
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
locase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']

print('''
1:Numbers only
2:Uppercase only
3:Lowercase only
4:Uppercase+Lowercase only
5:Uppercase+Lowercase+Digits
6:Mix Set''')
c=int(input("Your choice: "))

if c==1:
    passwordstack+=digits
elif c==2:
    passwordstack+=upcase
elif c==3:
    passwordstack+=locase
elif c==4:
    passwordstack+=upcase+locase
elif c==5:
    passwordstack+=upcase+locase+digits
elif c==6:
    passwordstack+=upcase+locase+digits+symbols
    
for i in range(0,n):
    password+=random.choice(passwordstack)

print("Your Random Password is :  ",password)
