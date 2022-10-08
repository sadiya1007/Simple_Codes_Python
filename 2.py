arr=[]
n=int(input("Enter the no of elements in the array "))

for i in range(0,n):
    #print("arr[",i,"]=",i+1)
    m=int(input())
    arr.append(m)
print(arr)

small = arr[0];

for i in range(0,len(arr)):
    if (arr[i]<small):
        small=arr[i]

print("Smallest number in Array is: ",small)
