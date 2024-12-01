# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# print the odd number of stars in a loop

# n=int(input("Enter the number: "))
# k=1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     k+=3
#     print()

# n=int(input())
# for i in range(0,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

n=int(input("Enter a number of rows: "))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print(j,end=" ")
    k+=2
    print()