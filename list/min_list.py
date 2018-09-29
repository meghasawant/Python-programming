#********** Program to find minimum and second minimum number from list.
def min_list(l):
	min_1 = l[0]
	min_2 = l[1]
	
	if min_2 < min_1:
		min_1 = l[1]
		min_2 = l[0]
	
	for y in l[2:]:
		if y < min_1:
			min_2 = min_1
			min_1 = y
		elif y < min_2:
			min_2 = y

	return min_1,min_2

def main():
	l = input("Enter list - ")
	print "Minimum and second minimum number is -",min_list(l)

if __name__=='__main__':
	main()
