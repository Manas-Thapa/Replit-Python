# Conditional operators
#else if
a=int(input("Enter your age:"))
print("Your age is:",a)
if a>=18:
  print('You are eligible to vote')
  print("yay")
else:
  print("You are not eligible to vote")
  print("Wait for",18-a,"years")
  #elif
  c=int(input("Enter Your No.:"))
  if c<0:
    print("Your Number Is Negative")
  elif c>0:
    print("Your Number Is Positive")
  else:
    print("Your Number Is 0")
    # nested if else
b=int(input("Enter Your Number:"))
if b<0:
  print("Your Number Is Negative")
  if b>=-10:
    print("Your Number Lies Between -10 to 0")
  elif b>=-20:
    print("Your Number Lies Between -20 to -10")
  else:
    print ("your number is less than -20")
elif b>0:  
 print("Your Number Is positive")
 if b>=10:
  print("Your Number Lies Between 10 to 0")
 elif b>=20:
    print("Your Number Lies Between 20 to 10")
 else:
    print ("your number is less than 20")
else:
  print("Your Number Is 0")
    



