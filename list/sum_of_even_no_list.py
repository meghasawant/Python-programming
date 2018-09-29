#******* Program to calculate sum of all even number of list(using bitwise operator find even number).

def even_sum(data):
	sum = 0
	for x in data:
		if (x & 1) == 0:
			sum += x
	return 	sum
	
def main():
	data = input("Enter number list -")
	print "Sum of even numbers of givan list is - ",even_sum(data)

if __name__=='__main__':
	main()




