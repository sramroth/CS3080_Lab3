import re
exercise = 1
while (exercise != 0):
	exercise = int(input("Which exercise would you like to test (1-8, 0 to exit)? "))

	#####################################################
	# Exercise 1: Validate Simple Zip Codes
	#####################################################
	if exercise == 1:
		zipcode = input("Enter a zip code: \n")
		zipCodeRegex = re.compile(r"^\d{5}$") 
		if zipCodeRegex.search(str(zipcode)) != None:
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 2: Extended Zip Codes
	#####################################################
	elif exercise == 2:
		zipcode = input("Enter a zip code: \n")
		extZipCodeRegex = re.compile(r"^\d{5}(-\d{4})?$")
		if extZipCodeRegex.search(str(zipcode)) != None:
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 3: Numerically Correct Zip Codes
	#####################################################
	elif exercise == 3:
		zipcode = input("Enter a zip code: \n")
		extZipCodeRegex2 = re.compile(r"^(0[1-9]|[1-9]\d)(\d{3}(-\d{4})?)$")
		if extZipCodeRegex2.search(str(zipcode)) != None:
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 4: Variable Name Validation
	#####################################################
	elif exercise == 4:
		name = input("Enter a variable name: \n")
		variableRegex = re.compile(r"^([a-z]|[A-Z]|_)(\w*)")
		if variableRegex.search(str(name)) != None:
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 5: Username Validation
	#####################################################
	elif exercise == 5:
		username = input("Enter a username: \n")
		userNameRegex = re.compile(r"^([a-z]|[A-Z])(\w+\.\w+)?(\w+)$")
		if userNameRegex.search(str(username)) != None:
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 6: Min/Max Length Username Validation
	#####################################################
	elif exercise == 6:
		username = input("Enter a username: \n")
		userNameRegex = re.compile(r"^([a-z]|[A-Z])\w{5,15}$")
		if userNameRegex.search(str(username)) != None:
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 7: Email Validator
	#####################################################
	elif exercise == 7:
		email = input("Enter a email address: \n")
		emailRegex = re.compile(r"^([a-z]|[A-Z])\w+(\w+\.\w+)?@(\w+\.\w{2,4})")
		if emailRegex.search(str(email)) != None:
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 8: Separate City, State and Zip
	#####################################################
	elif exercise == 8:
		address = input("Enter a city, state and zip: \n")
		# TODO: put your regex here
		# TODO: use the regex to pull of the city, state, and zip here

		print("City: ")	# TODO: add the city here
		print("State: ") # TODO: add the state here
		print("Zip: ") # TODO: add the zip here

	#####################################################
	# Invalid choice 
	#####################################################
	elif exercise == 0:
		exit

	else:
		print("Your response must be from 0 to 8, try again: ")
