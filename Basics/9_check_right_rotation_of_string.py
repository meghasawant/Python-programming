######### Assignment No.9- WAP to accept a 2 string from user & check if second string is right rotation of first string.

print " **** Ex.- Input - manager,germana, Output - True or False ****"
print

first = input("Enter the first string - ")

second = input("Enter the second string - ")

res = first+first	#Concatenate first string with itself
#print res

print second,"is right rotation of",first,"is",second in res



