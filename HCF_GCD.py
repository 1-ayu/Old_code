def HCF(a,b):
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if (a%i==0) and (b%i==0):
            hcf=i
    return hcf

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
# print("The GCD of the given numbers is :",HCF(a,b))

