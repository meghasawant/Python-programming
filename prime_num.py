# *********** Program to dislpay all prime numbers of a given range from user. *********** #

def prime(lb,ub):
	if (lb >= ub or lb <= 0):
		print "Range is invalid."

	else :
		if (lb == 1):
			lb +=1
		print " Prime numbers are - "

		for i in range(lb,ub+1):
			flag = 0

			for x in range(2,i):
				if (i % x == 0):
					flag = 1
					break
			if flag == 0:
				print i,			

def main():
	lb,ub = input("Enter the range to display prime numbers - ")
	prime(lb,ub)	

if __name__=='__main__':
	main()


