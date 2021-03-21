#Given a two Python list. Iterate both lists simultaneously such that list1 should 
# display item in original order and list2 in reverse order
#Given
#list1 = [10, 20, 30, 40]
#list2 = [100, 200, 300, 400]

num1=[10,20,30,40]
num2=[100,200,300,400]
i=0
j=1
while i<len(num1):
    while j<=len(num2):
        print(num1[i],num2[-j])
        j=j+1
        i=i+1
    
    