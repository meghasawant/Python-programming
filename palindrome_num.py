# ********** Program to check a given number is palindrome or not. **********

def palindrome(no):
	rev = 0
	while(no!=0):
		rem = no % 10
		rev = rem + (rev * 10) 
		no = no/10
	return rev

def main():
	no = input("Enter positive number :" )

	if (no <= 0):
		print "Entered number is non-positive."
	else:
		result = palindrome(no)	
		if (no == result):
			print no,"is Palindrome Number."
		else:
			print no,"is Not Palindrome Number."

if __name__=='__main__':
	main()

