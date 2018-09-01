######### WAP to accept a number from user & check if it's even or odd using bitwise.

print "**** To find out number is even or odd ****"

x = input("Enter the number : ")

if (x & 1) == 0:
	print x,"is even number."
else :
	print x,"is odd number."
