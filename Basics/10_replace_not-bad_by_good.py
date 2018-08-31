######### Assignment No.10- WAP to accept a 2 string from user & replace not-bad with good.

print " **** Ex.- Input - Python is not that bad , Output - Python is good ****"
print

string = input("Enter the first string - ")

s1=string.find("not")

s2=string.find("bad")
print s1,s2

print string.find("not") < string.find("bad") and string[:s1]+"good"+string[s2+3]

