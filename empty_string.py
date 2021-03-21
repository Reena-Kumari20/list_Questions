#remove function in list with while loop:
A=["A"," ","B","C"," "]
i=0
while i<len(A):
    if A[i]==" ":
        A.remove(A[i])
    i=i+1
print(A)

#remove function in list with for loop:
B=["a"," ","y"," "]
for x in B:
    if x==" ":
        B.remove(x)
print(B)

#in function

def list(l):
    for a in l:
        if a==" ":
            l.remove(a)
    return l
l=["3"," ","4"," "]
print(list(l))

