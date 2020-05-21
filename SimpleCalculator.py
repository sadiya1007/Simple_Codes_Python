def circle():
    r=int(input("Enter Radius: "))
    area=3.148*r*r
    p=2*3.14*r
    print("Area is : ",area)
    print("Perimeter is : ",p,"\n")
def rectangle():
    l=int(input("Enter Length : "))
    b=int(input("Enter Breadth : "))
    area=l*b
    p=2*(l+b)
    print("Area is : ",area)
    print("Perimeter is : ",p,"\n")
def square():
    s=int(input("Enter Side: "))
    area=s*s
    p=4*s
    print("Area is : ",area)
    print("Perimeter is : ",p,"\n")
def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print("Addition is: ",a+b)
def sub():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print("Subtraction is: ",a-b)
def divide():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print("Division is: ",a/b)
def mul(a,b):
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print("Multiplication is: ",a*b)
    
while True:
 print("The Options are:\n   1:Rectangle  2:Circle   3:Square\n   4:Addition   5:Subtract 6:Divide  7:Multiply  \n   0:Exit\n")
 opt=int(input("Choose: "))
 if opt==1:
     rectangle()
 elif opt==2:
     circle()
 elif opt==3:
     square()
 elif opt==4:
     add()
 elif opt==5:
     sub()
 elif opt==6:
     divide()
 elif opt==7:
     mul()
 elif opt==0:
     print("Exit initiated")
     break
 else:
    c='Invalid'
