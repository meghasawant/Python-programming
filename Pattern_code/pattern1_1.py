'''
Pattern -
	* 
	* * 
	* * * 
	* * * * 
'''

def pattern(rows,ch):
	for i in range(1,rows+1):
		for _ in range(i):
			print ch,
		print ""


def main():
	n = input("Enter number of rows to print pattern - ")
	ch = raw_input("Enter any character input to print in pattern - ")
	pattern(n,ch)

if __name__=='__main__':
	main()
