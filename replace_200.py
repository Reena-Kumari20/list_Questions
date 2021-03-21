#Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
#Given

list1 = [5, 10, 15, 20, 25, 50, 20]
#Expected output:
#list1 = [5, 10, 15, 200, 25, 50, 20]
index=list1.index(20)
list1[index]=(200)
print(list1)

list2= [5, 10, 15, 20, 25, 50, 20]
if 20 in list2:
     list2.remove(20)
     list2.insert(3, 200)

print(list2)