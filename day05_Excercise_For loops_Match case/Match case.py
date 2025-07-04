# Match case
x=int(input())
match x:
   case 0:
     print("x is zero")
   case 1:
     print("x is One")
   case 2:
     print("x is Two")
   case 3:
     print("x is Three")
   case _ if x!=10:
     print("x is not 10")
   case _ if x==10:
     print("x is 10")
   case _:
     print("x is ",x)