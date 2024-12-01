s="Ayush raj karan is the great boy and the great person"
l=s.split()
k=[]
for i in l:
    # if condition is used to store unique string
    #  in another list 'k'
    if(s.count(i)>1 and (i not in k)or s.count(i)==1):
        k.append(i)
print(' '.join(k))