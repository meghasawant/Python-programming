# ********** Program to display reverse order of a given number. **********

def rev(no):
	rev = 0
	while(no!=0):
		rem = no % 10
		rev = rem + (rev * 10) 
		no = no/10
	return rev

def main():
	no = input("Enter positive number :" )

	if (no <= 0):
		print "Entered number is non-positive"
	else:
		print "Reverse number of",no,"is",rev(no)

if __name__=='__main__':
	main()

