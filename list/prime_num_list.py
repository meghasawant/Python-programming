#******** Program to find all prime numbers from given list.

def prime(data):
	result = []
	for x in data:
		flag = 0
		if(x<2):
			flag = 0 
		elif (x==2 or x==3):
			flag = 1 
		elif (x% 2==0):
			flag = 0 
		else:
			for y in xrange(3,int(x//2)+2,2):
				if x % y == 0:
					flag = 0 
				else:
					flag = 1
		if flag ==1:
			result.append(x)
	return result		
	
def main():
	data = input("Enter number list -")
	print prime(data)

if __name__=='__main__':
	main()




