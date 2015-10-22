var2="changeme"
x=0
while x<=4:
    var1=input("enter password")
    if var1==var2:
       print("correct")
       break
    elif var1!=var2:
         print("try again")
         x=x+1
    if x==5:
         print("Access Denied")
         break
