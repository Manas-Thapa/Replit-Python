# String Methods
# Strings are immutable
a=" Manas!!! Manas"
print(a)
print(a.upper())
print(a.lower())
print(a.strip())
print(a.rstrip("!"))#does not strip leading characters
print(a.replace("nas","ngo")) #Replaces all occurences
print(a.split(" ")) #splits at given instance and returns a list
apple="hello woRld"
print(apple.capitalize()) # It capitalizes the first letter of the string and makes the rest of the strin lowercase
print(apple.center(50,"-")) #It centers the string and fills the remaining spaces with the provided character
print(a.count("a"))#counts the number of occurences of th e given character
print(a.endswith("a",0,5))#It checks if the string ends wth the given character
print(a.find("M"))#It returns the index of the first occurence of the given character
print(a.find("l"))
print(a.index("M"))
b="hello00\n"
print(b.isalnum())
print(b.isalpha())
print(b.islower())
print(b.isprintable())
c="    "
print(c.isspace())
d="Lol Lol is"
print(d.istitle())
print(d.isupper())
print(d.startswith("L",4))
print(d.swapcase())
print(d.title())


