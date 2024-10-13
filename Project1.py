list1=['math','physics','chemistry',90,88,91]
tuple1=('apple','orange','banana','peach',3,1,2,4)

print(list1)
print(tuple1)
print()
print(list1[3])
print()
list1.insert(3,'biology')
print(list1)
list1.insert(7,98)
print(list1)
print()

list2d=[['raed','sami','dami'],[10,20,30],[20,30,40]]

print(list2d[0][0],"has a score of ",list2d[1][0])
print(list2d[0][1],"has a score of ",list2d[2][1],"on him")
print()
list3=[100,201,-23,0,11,97,201]
list3.append(99)
print(list3)
list3.pop(4)
print(list3)
print(list3.count(201))
