######### Assignment No.8- WAP to accept a 2 string from user & jumble them, swap first 2 character of both.

print "**** Ex.- Input - dog,dinner, Output - dig,donner ****"

first = input("Enter the first string - ")

second = input("Enter the second string - ")

f1 = first[:2]	#First 2 character of string

s1 = second[:2]
#print f1," ",s1

print "Output String is - ",first.replace(f1,s1)," ",second.replace(s1,f1)

