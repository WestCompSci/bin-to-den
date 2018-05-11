which = input ("WOULD YOU LIKE TO DO BINARY --> DENARY(1) OR DENARY --> BINARY(2)?  ")
if which == "1":
	binary = input("PLEASE ENTER A BINARY NUMBER: ")
	decimal = 0
	for digit in binary:
		decimal = decimal*2 + int(digit)
	print ("YOUR NUMBER IN DENARY IS: " + str(decimal))

elif which == "2":
	denary = input("PLEASE ENTER A DENARY NUMBER: ")
	denary = int(denary)
	denary = bin(denary)
	print ("YOUR NUMBER IN BINARY IS: " + str(denary))

else:
	print ("ERROR")
