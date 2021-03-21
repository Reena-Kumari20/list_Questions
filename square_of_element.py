#Exercise 3: Given a Python list of numbers. Turn every item of a list 
# into its square
#Given:

list1 = [1, 2, 3, 4, 5, 6, 7]
#Expected output:

#[1, 4, 9, 16, 25, 36, 49]

i=0
a=[]
while i<len(list1):
    b=list1[i]**2
    a.append(b)
    i=i+1
print(a)