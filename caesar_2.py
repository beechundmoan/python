"""

	The ASCII character set is pretty big, and our uppercase
	alphabet only uses ASCII codes from 65-90. 
	
	Our first version of this script is pretty dumb: note the
	non-alphabet characters in our original output string.


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
	#	Make sure that we stay in the 65-90 range
	if new_ascii_code > 90:
		new_ascii_code = new_ascii_code - 25
	#	Convert our new ascii code back to a character
	new_character = chr(new_ascii_code)
	#	Add our new character to the end of our output string
	output_string = output_string + new_character

print(output_string)