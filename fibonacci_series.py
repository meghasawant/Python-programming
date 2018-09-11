# ********** Program to display the fibonacci series upto a given number. **********

def fib(num):
	f1,f2,f3 = 0,1,1
	print f1,
	for i in range(0,num):
		while(f3 <= num):
			print f3,
			f3 = f1 + f2
			f1,f2 = f2,f3

def main():
	num = input("Enter a positive number:" )

	if (num < 0):
		print "Number you've entered is non-positive."
	else:
		print "Fibonacci Series upto",num,"is"
		fib(num)

if __name__=='__main__':
	main()

