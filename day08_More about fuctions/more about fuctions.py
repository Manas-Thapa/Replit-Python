def avg(a=100,b=20):
  print("The average is",(a+b)/2)
avg()
avg(1)
avg(b=21,a=5)
avg(1,80)


def aveg(*numbers):
  sum=0
  for i in numbers:
   sum=sum+i
  print("Average is ",sum/len(numbers))


aveg(1,2,4,6,9,42,2,2)
def name(**name):
  print("Hello ",name["fname"],name["mname"],name["lname"])
name(mname="hll",fname="ll",lname="lll")


def averag(*numbers):
  sum=0
  for i in numbers:
   sum=sum+i
  return sum/len(numbers)
c = averag(111,31,3,2,312) 
print(c)