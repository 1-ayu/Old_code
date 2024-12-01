n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


# It is also done by defining a function

# def pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1)+'*'*(2*i+1))
# pyramid(4)