# import array as myarray
# arr=[1,2,3,4,5]
# arr2=[1.4,3.2,5.3,3.0]

# for i in range(0,len(arr)):
#     print(arr[i],end=' ')
# print("\n")
# for i in range(0,len(arr2)):
#     print(arr2[i],end=' ')
import array as myarray
# Assessing array
# a=list(range(1,25,2))
# print(a)
# new_array=myarray.array('i',a)
# for i in range(0,len(new_array)):
#     print(new_array[i],end=' ')
# print("\n")

# print(new_array)

new_arr=myarray.array('i',[1,2,3,4,5,6])
for i in range(0,len(new_arr)):
    print(new_arr[i],end=' ')
print(new_arr,end=' ')
print("\n")
new_arr.insert(0,232)
for i in range(0,len(new_arr)):
    print(new_arr[i],end=' ')
