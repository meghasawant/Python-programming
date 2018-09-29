#********** Program to return list of number which appeared in fibonacci series.

def fibonacci(data):
	result = []
	upper_bound = max(data)

	f1,f2,f3 = 0,1,1
	result.append(f1)

	for i in range(0,upper_bound):
		while(f3 <= upper_bound):
			result.append(f3)
			f3 = f1 + f2
			f1,f2 = f2,f3

	i=0
	result1 = []

	while i < (len(data)):
		if data[i] in result:
			result1.append(data[i])	
			i +=1
		else:
			i +=1	
	return result1

def main():
	data = input("Enter a number list : ")

	print "Fibonacci numbers which appeared in given list are -",fibonacci(data)

if __name__=='__main__':
	main()

