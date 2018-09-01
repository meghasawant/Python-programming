######### WAP to accept a number from user & check if it's multiple of 16 or not using bitwise.

print "To find out multiple of 16 "

x = input("Enter the number : ")

if (x & 3) == 0:
	print x,"is multiple of 16."
else :
	print x,"is not multiple of 16."
