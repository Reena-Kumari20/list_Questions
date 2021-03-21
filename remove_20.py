#Exercise 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
#Expected output:

#[5, 15, 25, 50]

i=0
while i<len(list1):
    if list1[i]==20:
        list1.remove(list1[i])
    i=i+1
print(list1)

list2=[5,20,15,20,25,50,20]
for x in list2:
    if x==20:
        list2.remove(x)
print(list2)