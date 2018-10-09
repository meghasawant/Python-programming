#********************** Display Function **********************

def display(dict_data):
	for x in dict_data:
		if type(dict_data[x]) == list:
			for i in dict_data[x]:
				print x,":",i
		else:
			print x,":",dict_data[x]

#********************** Search Function **********************

def search(dict_data,key,value):
	if key in dict_data:
		flag = 1
		if type(dict_data[key]) == list:
			for i in dict_data[key]:
				if i == value:
					flag = 0
		else:
			if dict_data[key] == value:
				flag = 0

		if flag == 0:
			print "Data is present in dictionary."
		else:
			print "Data is not present in dictionary."
	else:
		print "Key is not present in dictionary."

#********************** Update Function **********************

def update(dict_data,key,value):
	if key in dict_data:
		if type(dict_data[key]) == list:
			for i in dict_data[key]:
				print key,":",i
			key_value = dict_data[key]
			val = input("Enter which value you want to update from above data - ")
			if val in key_value:
				i = 0
				while i < len(key_value):
					if key_value[i] == val:
						key_value[i] = value
					else:
						i +=1
			else:	
				key_value.append(value)
	else:
		dict_data[key] = value	
	return dict_data

#********************** Append Function **********************

def append(dict_data,key,value):
	if key in dict_data:
		if type(dict_data[key]) == list:
			if value in dict_data[key]:
				print "Data is available in dictionary."
			else:
				key_value = dict_data[key]
				key_value.append(value)
		else:
			if value in dict_data:
				print "Data is available in dictionary."	
			else:
				key_value = []
				key_value.append(dict_data[key])
				key_value.append(value)
				dict_data[key] = key_value
	else:
		dict_data[key] = value
	return dict_data

#********************** Delete Function **********************

def delete(dict_data,key,value):
	if key in dict_data:
		if type(dict_data[key]) == list:
			key_value = dict_data[key]
			i = 0
			while i < len(key_value):
				if key_value[i]==value:
					del(key_value[i])
				else:
					i +=1	
			if len(key_value) == 1:	
				val = key_value[0]
				dict_data[key] = val				
		else:		
			del(dict_data[key])
	else:
		print "Given key is not present in dictionary."
	return dict_data

#********************** Menu Function **********************

def menu(dict_data):
	print "\n*********** Operations on Dictionary ***********"
	print " 1. Display Dictionary \n 2. Search Dictionary \n 3. Update Dictionary \n 4. Append Dictionary \n 5. Delete Dictionary \n 6. Exit"
	ch = input("*** Enter your choice - ")
	operations(ch,dict_data)

#********************** Operations Function **********************

def operations(ch,dict_data):
	if ch == 1:
		print "Display Dictionary"
		display(dict_data)

	elif ch == 2:
		print "Search Dictionary"
		key,value = input("Enter the key and value to search -")
		search(dict_data,key,value)

	elif ch == 3:
		print "Update Dictionary"
		key,value = input("Enter the key and value to update -")
		print update(dict_data,key,value)

	elif ch == 4:
		print "Append Dictionary"
		key,value = input("Enter the key and value to append -")
		print append(dict_data,key,value)

	elif ch == 5:
		print "Delete Dictionary"
		key,value = input("Enter the key and value to delete -")
		print delete(dict_data,key,value)

	else:
		exit(0)

	menu(dict_data)

#********************** Main Function **********************

def main():	
	dict_data=input("Enter the dictionary to perform operations - ")
	menu(dict_data)

if __name__=='__main__':
	main()



