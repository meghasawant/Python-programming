'''
Pattern -
	      1 
	    2 1 2 
	  3 2 1 2 3 
	4 3 2 1 2 3 4 
'''

def pattern(rows):
	for i in range(1,rows+1):
		b = 0 + i
		for _ in range(rows-i):
			print " ",
		for j in range(2*i-1):
			print b,
			if j < i-1:
				b = b - 1
			else:
				b = b + 1
		print ""


def main():
	n = input("Enter number of rows to print pattern - ")
	pattern(n)

if __name__=='__main__':
	main()
