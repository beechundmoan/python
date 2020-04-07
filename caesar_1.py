"""

	This quick and dirty python script demonstrates a simple Caesar cipher

	Caesar ciphers use a "rotated alphabet" to implement very simple encryption:


	CIPHER KEY
	=======
	
	A B C D E F  G H  I  J  K  L M N O P Q R S T U V W X Y Z
	R S T U V W X Y  Z A B  C D E F G H  I  J  K L M N O P Q
	
	=======
	
	WIGGLES = NZXXCVJ


"""


#	Our input string:
string_to_encode = "HELLO WIGGLES"

#	Our output string (just an empty container right now)
output_string = ""

#	Set our alphabet rotation offset
character_offset = 6

#	Step through our input string, character by character
for character in string_to_encode:
	#	Convert our character to its ascii code (capital A=65)
	ascii_code = ord(character)
	#	Add our offset to the original character
	new_ascii_code = ascii_code + character_offset
	#	Convert our ascii code back to a character
	new_character = chr(new_ascii_code)
	#	Add our new character to the end of our output string
	output_string = output_string + new_character

print(output_string)