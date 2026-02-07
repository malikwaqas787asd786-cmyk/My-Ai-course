# conditonal statement
# wap to find greatest of 4 numbers enter by the user?

a=int(input("enter first num:"))
b=int(input("enter second num:"))
c=int(input("enter third num:"))
d=int(input("enter fourth num:"))

if(a>=b and a>=c and a>=d):
    print("first num is greater",a)
elif(b>=c):
    print("second num is greater",b)
elif(c>=d):
    print("thired num is greater",c)
else:
    print("fourth num is greater",d)

    print("ends here")        
