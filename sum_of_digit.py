# ********** Program to display the sum of digits of a given number. **********

def sum(x):
	sum = 0

	while(x != 0):
		sum += (x % 10)
		x = x/10
	return sum

def main():
	x = input("Enter a positive number:" )

	if (x <= 0):
		print "Number you've entered is non-positive."
	else:
		print "Sum of digits of a number",x,"is",sum(x)

if __name__=='__main__':
	main()

