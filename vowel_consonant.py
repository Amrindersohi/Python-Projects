strng=input("Enter a string : ")
a=b=0
for i in strng:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        a+=1
    else:
        b+=1
print("Vowels =",a)
print("Consonant =",b)
