# y=int(input("Enter year : "))
# if (y%4==0):
#     if(y%100==0):
#         if(y%400==0):
#             print(y,"is the leap year")
#         else:
#             print(y,"is not a leap year")
    
#     else:
#         print(y,"is a leap year")
# else:
#     print(y,"is not a leap year")
## Leap Year 

year=int(input("Enter the year:"))
if (year%4)==0:
	if(year%100)==0:
		if(year%400)==0:
			print(year,"is a leap year")
		else:
			print(year,"is a not leap year")
	else:
		print(year,"is a leap year")
else:
	print(year,"is not a leap year")
