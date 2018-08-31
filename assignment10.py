#Q.1- Write a python code to find a valid email address from a text.
import re
a=input("Enter the Email:")
j=0
b=re.finditer("^[a-zA-Z]{1}[_a-zA-Z0-9.]*[@]{1}['gmail.com''yahoo.com']{9,9}$",a)
for m in b:
    j=m.group()
if a==j:
    print("Email is Valid:")
else:
    print("Email is not Valid:")
#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
a=input("Enter The Phone No:")
j=0
b=re.finditer("^[+]{1}[9]{1}[1]{1}[6789]{1}\d{9}$",a)
for m in b:
    j=m.group()
if a==j:
    print("Phone is Valid:")
else:
    print("Phone is not Valid:")
