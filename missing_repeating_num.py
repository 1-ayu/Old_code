"""Method 3
* (Use elements as Index and mark thevisited places)
    Traverse the array. While traversing,use the absolutee value of every element as an index and mark the value
    at this index as negative to mark it visited. If something is already marked negative then this is the repating 
    element . To find missing, traverse the array again and look for a positive value."""

def printTwoElements(arr,size):
    for i in range(size):
        if arr[abs(arr[i])-1]>0:
            arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        else:
            print("The repeating element is : ",abs(arr[i]))
    for i in range(size):
        if arr[i]>0:
            print("The missing element of ", i+1)
        
arr=[7,3,2,1,4,4,5]
n=len(arr)
printTwoElements(arr,n)

# #  Taking input as a list

# list=[]
# n=int(input("Enter number of elements :"))
# for i in range(0,n):
#     ele=int(input())
#     list.append(ele)

# print(list)