"""
	All of our previous examples had a hard-coded string
	to encode, which works as an example, but is a pain to re-use.
	
	Reusability is a HUGE focus of programming, so let's make it so that
	we can enter our own string to encode.
	
	We could easily handle lowercase *and* uppercase characters,
	but I'll leave that task to your imagination. We'll deal only
	in uppercase, for the sake of brevity.
	
"""


#	Ask for an input string, and insert it into our variable.
string_to_encode = input("Please enter a message to encode! [ PRESS ENTER TO ENCODE ] :")

#	Convert our whole string to uppercase
string_to_encode = string_to_encode.upper()


#	For the purpose of this script, nothing else needs to change!
output_string = ""
no_translate = "., ?!"
character_offset = 6

for character in string_to_encode:
	if character in no_translate:
		new_character = character
	else:
		ascii_code = ord(character)
		new_ascii_code = ascii_code + character_offset
		if new_ascii_code > 90:
			new_ascii_code -= 25
		new_character = chr(new_ascii_code)
	output_string += new_character

print(output_string)