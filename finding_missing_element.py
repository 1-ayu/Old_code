arr=[1,2,3,4,5]
arr1=[5,3,2,1]

#  Brute force approach

# def finder(arr,arr1):
#     return sum(arr)-sum(arr1)
# print(finder(arr,arr1))

#  Optimized approach

# def finder(arr,arr1):
#     # sort the arrays
#     arr.sort()
#     arr1.sort()

#     # Compare elements in the sorted arrays
#     for a,b in zip(arr,arr1):
#         if a!=b:
#             return a
#     return arr()
# print(finder(arr,arr1))

def finder(arr,arr1):
    arr.sort()
    arr1.sort()

    for i,j in zip(arr,arr1):
        if i!=j:
            return i
    return arr()
print(arr,arr1)
print(finder(arr,arr1))