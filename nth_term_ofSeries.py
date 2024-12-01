#  1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187....
#  Find the nth term

num=int(input("Enter a number: "))
if (num%2)==0:
    num=num//2
    print(3**(num-1))
else:
    num=num//2
    print(2**(num))