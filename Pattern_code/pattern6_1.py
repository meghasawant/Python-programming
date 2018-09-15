'''
Pattern -
	D C B A B C D 
	  C B A B C 
	    B A B 
	      A 
'''
def pattern(rows):
	for i in range(rows):
		b = 64 + rows
		for _ in range(i):
			print " ",
		for j in range(2*rows-1):
			print chr(b),
			if j < rows-1:
				b -= 1
			else:
				b += 1
		rows -=1
		print ""

def main():
	n = input("Enter number of rows to print pattern - ")
	pattern(n)

if __name__=='__main__':
	main()


