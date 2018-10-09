def menu(list1,list2):
	print "\n************************** \n Menu for set operatios on list "
	print " 1. Union \n 2. Intersection \n 3. Difference \n 4. Symmetric difference \n 5. Exit"
	ch = input("*** Enter your choice - ")
	set_operation(ch,list1,list2)
	
def set_operation(ch,list1,list2):
	if ch == 1:
		print "Union"
		for i in list1:
			print i,
		for j in list2:
			if j not in list1:
				print j,

	elif ch == 2:
		print "Intersection"
		for i in list1:
			if i in list2:
				print i,			
	elif ch == 3:
		print "Difference"
		for i in list1:
			if i not in list2:
				print i,			

	elif ch == 4:
		print "Symmetric difference"
		for i in list1:
			if i not in list2:
				print i,
		for j in list2:
			if j not in list1:
				print j,
			
	else:
		exit(0)

	menu(list1,list2)


def main():
	list1 = input("Enter list 1 -")
	list2 = input("Enter list 2 -")
	menu(list1,list2)

if __name__=='__main__':
	main()



