num=int(input("enter the number to create number table:"))
lst=[]
for i in range(1,11):
    lst.append(i)
lst1=list(map(lambda n1:n1*num,lst))
print(lst1)