'''
Write a Python program to accept a string from the user and create a menu to check
a. Whether it is palindrome or not.
b. Display number of characters,
c. No of words,
d. No.of lower case letters,
e. No. Of uppercase letters
f. No. of digits in the string.
'''
a=input("enter a string")
lowercount=uppercount=0
digitcount=wordcount=0
d=len(a)
c=a[::-1]
for i in a:
    if i.islower():
        lowercount+=1
    if i.isupper():
        uppercount+=1
    if i.isdigit():
        digitcount+=1
    if i.isalpha():
       wordcount+=1
       
    else:
        print()
            
            
            
i='y'   
while i=='y':        
    b=int(input("MENU:\n1)Whether it is palindrome or no.\n2) Display number of characters,\n3) No of words,\n4) No.of lower case letters,\n5) No. Of uppercase letters\n6) No. of digits in the string."))
    if b==1:
        if a==c:
            print('True')
        else:
            print('False')
    if b==2:
        print('No.of charecters',d)
    if b==3:
        print('No.of words',wordcount)
    if b==4:
        print('No.of lowercase letters',lowercount)
    if b==5:
        print('No.of uppercase letters',uppercount)
    if b==6:
        print('No.of digits',digitcount)
    else:
        print()
    i=input('Would u lyk to continue?(y/n)')
