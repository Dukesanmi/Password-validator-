#password validator
#password must have at least
password=input('Enter password: ')

def validator(input):
	if hasUppercase(input):
		print('hasUppercase check')
	else:
		print('INVALID! Password must contain uppercase character')
	if hasLowercase(input):
		print('hasLowercase check')
	else:
		print('INVALID! Password must contain lowercase character')
	if hasSpecialcharacter(input):
		print('hasSpecialcharacter check')
	else:
		print('INVALID! Password must contain a symbol')
	if hasNumber(input):
		print('hasNumber check')
	else:
		print('INVALID! Password must contain a numeric character')
	if has8Characters(input):
		print('has8Characters check')
	else:
		print('INVALID! Password should have at least 8 characters')
	if hasUppercase(input) and hasLowercase(input) and hasSpecialcharacter(input) and hasNumber(input) and has8Characters(input) is True:
	    print('Password is valid')
	else:
	    print('Password invalid')    

	#elif hasUppercase(input) and hasLowercase(input) and hasSpecialcharacter(input) and hasNumber(input) and has8Characters(input) is not True:

#1 uppercase character
def hasUppercase(input):
    for character in input:
        if character==character.upper():
        	return True
 #1 lowercase character
def hasLowercase(input):
 	for character in input:
 		if character==character.lower():
 			return True
#1 special character
def hasSpecialcharacter(input):
	specialCharacter=['!','@','#','$','%','^','&','*','(',')','-','_','+','=']
	for character in input:
		for char in specialCharacter:
			if character==char:
				return True
#1 number 
def hasNumber(input):
	number=range(0,10)
	for character in input:
		for char in number:
			char=str(char)
			if character==char:
				return True
#has at least 8 characters
def has8Characters(input):
	if len(input)>=8:
		return True
print(validator(password))



