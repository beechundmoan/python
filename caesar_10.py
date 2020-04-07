"""
	All of our previous scripts interrupt the program to ask for user input,
	which can be useful, but isn't very flexible.
	
	What if we wanted to compare the same string encoded with two
	different offsets? We'd have to type the same string in twice.
	
	DRY!

	All we need to do is specify another argument to our function.
	It doesn't matter which order our arguments are *defined* in,
	but when we call the function later, we have to match the same order.
	Arguments must be separated by a comma.
	
"""

def encode_string(string_to_encode, character_offset=6):
	"""
	
		Notice that we didn't define a default value for string_to_encode, but we did for character_offset.
		Our function will fail if we don't specify a string_to_encode, as it probably should.
		
	"""
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
	

print("Yet another Caesar Cipher script!")

input_string = input("Enter a message to encode: ")

offset_default = encode_string(input_string)

offset_custom	= encode_string(input_string, 14)

print(offset_default)
print(offset_custom)
