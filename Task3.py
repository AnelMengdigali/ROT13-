
#Task3: symmetric encryption algorithm (type of Caeser Cipher)
def menu3():

	print("         Welcome to the symmetric encryption          ")
	rotation = input("Choose the rotation factor for symmetric encryption (indicate integer number): ")
	phrase = input("Please enter your phrase: ")
    
	return int(rotation), phrase

def caesarCipher(integer, string):

	ccipher = ''

	#doing a shift for each letter:
	for char in string:

		if char == ' ': 
			ccipher = ccipher + char
		elif char.isupper():
			ccipher = ccipher + chr( ( ( ord(char) + integer - 65 ) % 26 ) + 65 )
		elif char.islower():
			ccipher = ccipher + chr( ( ( ord(char) + integer - 97) % 26 ) + 97 )

	return ccipher

rotation, text = menu3()

print("The encrypted text: ", caesarCipher(rotation, text))
