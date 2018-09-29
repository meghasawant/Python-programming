#********** Program to perform Selection sort in given list.

def sort_list(l):
	len_l = len(l)
	j=0
	while j < len_l:
		y=0
		while y+1 < len_l:
			if l[y] > l[y+1] :
				temp = l[y+1]
		        	l[y+1] = l[y] 
				l[y] = temp
			y += 1
		j += 1

	return l

def main():
	l = input("Enter list - ")
	print sort_list(l)

if __name__=='__main__':
	main()
