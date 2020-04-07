"""
	We've made a MAJOR error in all of our previous functions!
	
	What happens if we just call our encode_string() function without
	specifying an offset?
	
	Our program complains and refuses to run - which isn't very useful
	or flexible.
	
	We can account for this in one of a few ways, the simplest of which
	is to specify a default value when defining our function.

"""

def encode_string(character_offset=6):
	string_to_encode = input("Please enter a message to encode! [ PRESS ENTER TO ENCODE ] :")
	string_to_encode = string_to_encode.upper()
	output_string = ""
	no_translate = "., ?!"
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
	return(output_string)
	

print("Welcome to our fourth Caesar Cipher script")

#	Encodes our input string with the default offset of 6
with_default = encode_string()

#	Encodes our string with our specified offset
with_custom_offset = encode_string(21)

#	Hmm, if we want to encode the same message in two different ways....
