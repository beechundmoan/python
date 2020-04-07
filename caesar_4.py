"""
	Our last script handled the space character perfectly,
	but what if we need other punctuation marks?
	
	We could create an IF statement for each mark, 
	but that makes for long, unwieldy code.
	
	The following is much, much easier to implement, modify and read.
	Below, look for a new variable called no_translate - this string of
	characters represents characters we'll just add directly to our output
	string when we find them.
	
"""


#	Our input string:
string_to_encode = "HELLO WIGGLES, HOW ARE YOU?"

#	Our output string (just an empty container right now)
output_string = ""

#	Our list of "no translate" characters
no_translate = "., ?!" 

#	Set our alphabet rotation offset
character_offset = 6

#	Step through our input string, character by character
for character in string_to_encode:
	if character in no_translate:
		#	If the character is in our no_translate list, add it directly to output
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