def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def divide(a,b):
    return a/b
def mul(a,b):
    mult=a*b
    return mult
while True:
 m=int(input("Enter a: "))
 n=int(input("Enter b: "))
 print("The Options are:\n   1:Add\n   2:Subtract\n   3:Divide\n   4:Multiply\n   5:Exit\n")
 opt=int(input("Choose: "))
 if opt==1:
    c=add(m,n)
 elif opt==2:
     c=sub(m,n)
 elif opt==3:
     c=divide(m,n)
 elif opt==4:
     c=mul(m,n)
 elif opt==5:
     print("Exit initiated")
     break
 else:
    c='Invalid'
 print('The result is : ',c)


