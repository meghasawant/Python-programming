######### Assignment No.7- WAP to accept a string from user & replace the occurences of first character in remaining part of string with *.

print "**** Ex.- Input - babble, Output - ba**le ****"

s = input("Enter the string - ")

s1 = s[:1]	#First character of string
#print s1,""

s2 = s[1::]	#Sub-string from second index position
#print s2

print "Output String is - ",s1+s2.replace(s1,'*')	#replace character by * and combine the string

