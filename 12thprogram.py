# wap to cheak if a list contains a palindrom of elements.
# (hint:use copy() method)?
list1=[1,2,3]
list2=[1,2,1]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
   print("palindrom")
else:
   print("not palindrom")   
