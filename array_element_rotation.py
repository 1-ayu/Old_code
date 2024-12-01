# Method 1: The Brute force Method
def rotleft(a,d):
    temp=[]
    temp.extend(a[0:d])
    del a[0:d]
    a.extend(temp)
    return a

a=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    k=int(input())
    a.append(k)
print(a)
d=int(input("Enter the number of rotation: "))

print(rotleft(a,d))