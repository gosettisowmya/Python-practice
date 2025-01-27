a=int(input("enter the first value a:"))
b=int(input("enter the second value b:"))
c=int(input("enter the third value c:"))
if(a>b):
    if(a>c):
        print(a,"is the largest number")
    else:
        print(c,"is the largest number")
else:        
    if(b<c):
        print(b,"is the largest number")
    else:
        print (c,"is the largest number")          