"""

	We're getting there, but we still have (at least) one non-alphabetic
	character! 
	
	All of our punctuation and whitespace are also represented in
	ASCII, and to make things a little more interesting, some
	of those ASCII codes are less than 65 or greater than 90!
	
	For this version of our code, let's look at handling just
	the space character.

"""


#	Our input string:
string_to_encode = "HELLO WIGGLES"

#	Our output string (just an empty container right now)
output_string = ""

#	Set our alphabet rotation offset
character_offset = 6

#	Step through our input string, character by character
for character in string_to_encode:
	if character is " ":
		#	If the character is a space, just add it directly to our output
		output_string = output_string + character
		#	Skip over the rest of the instructions here and continue to the next character
		continue
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