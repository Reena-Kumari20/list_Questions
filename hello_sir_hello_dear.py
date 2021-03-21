#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
a=[]

i=0
while i<len(list1):
    j=0
    while j<len(list2):
        x=(list1[i]+list2[j])
        a.append(x)
        j=j+1
    i=i+1
print(a)