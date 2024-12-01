# def pair_sum(arr,k):
#     if len(arr)<2:
#         return 
    
#     seen=set()
#     output=set()

#     for num in arr:

#         target =k-num

#         if target not in seen:
#             seen.add(num)
#         else:
#             output.add(min(num,target) or max(num,target))
            
    
#     return len(output)
# pair_sum([1,2,3,2],4)

from itertools import combinations
def my_pair_sum(arr,s):
    count=0
    comb=combinations(arr,2)
    for i in comb:
        if sum(i)==s:
            print(i)
            count+=1
        return count
print(my_pair_sum([1,2,3,2],8))
