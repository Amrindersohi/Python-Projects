strng=input("Enter the string:")
s2=''
for i in range(0,len(strng)):
    if('a'<=strng[i]<='z'):
        s2+=chr(ord(strng[i])-32)
    elif('A'<=strng[i]<='Z'):
        s2+=chr(ord(strng[i])+32)
    else:
        s2+=strng[i]
print(s2) 