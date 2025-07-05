# WHILE LOOPS

# INCREMENTING LOOP

i=0
while i<=6 :
   print(i)
   i=i+1
print("\nDone with loop")

# DECREMENTING LOOP

f=10
while f>=6 :
   print(f)
   f=f-1
print("\nDone with loop")

#Input loop

A=int(input("\nENTER A NUMBER : "))
while (A<=91) :
  A=int(input("\nENTER A NUMBER : "))
  print (A)
else:
  print ("\nNumber is greater than 91")
print("\nDone with loop")

# DO WHILE LOOP

b=int(input())
while b:
  print(b+1)
  if not (b<=91):
   break