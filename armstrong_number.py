#  Arstrong number -> abcd..= a^n+b^n+c^n+..
#  Example: 153 -> 1*1*1 + 5*5*5 + 3*3*3 = 153(The number itself)

lower=100
upper=1000
for i in range(lower,upper+1):
    order=len(str(i))
    s=0
    temp=i
    while temp>0:
        digit = temp%10
        s+= digit**order
        temp//=10
    if i==s:
        print(i)