# ********** Program to accept a number from user and check if it's armstrong number or not. **********

def armstrong(no):
	sum = 0
	while(no != 0):
		no1 = no % 10
		sum = sum + (no1 ** 3)
		no = no/10
	return sum

def main():
	no = input("Enter a positive number:" )
	if (no <= 0):
		print "Number you've entered is non-positive."
	else:
		result = armstrong(no)	
		if (no == result):
			print no,"is an armstrong number."
		else:
			print no,"is not an armstrong number."

if __name__=='__main__':
	main()

