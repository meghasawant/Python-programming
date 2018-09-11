# ********** Program to display the sum of even digits and odd digits of a given number. **********

# Function to calculate even and odd digits sum
def sum(no):
	even_sum = 0
	odd_sum  = 0

	while(no != 0):
		x = no % 10
		if (x % 2 == 0):
			even_sum += x
		else:
			odd_sum += x
		no = no/10

	print "Sum of Even digits is",even_sum
	print "Sum of Odd digits is",odd_sum

# Main function defination
def main():
	num = input("Enter a positive number:" )

	if (num <= 0):
		print "Number you've entered is non-positive."
	else:
		sum(num)

# Main function
if __name__=='__main__':
	main()

