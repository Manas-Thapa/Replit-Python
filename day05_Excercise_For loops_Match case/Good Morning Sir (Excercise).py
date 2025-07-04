# Exercise :Good Morning Sir
import time
timestamp=int(time.strftime("%H"))
if timestamp>=4 and timestamp<=12 :
  print("Good Morning Sir")
elif timestamp>=12 and timestamp<=16 :
  print("Good Afternoon Sir")
elif timestamp>=16 and timestamp<=20 :
  print("Good Evening Sir")
else :
  print("Good Night Sir")