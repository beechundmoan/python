"""
	All of our previous examples have a hard-coded offset - 
	which is fine, but not very flexible. What if we wanted to 
	be able to encode a bunch of different strings with different
	offsets?
	
	Functions have a great feature for exactly this purpose, called
	"Arguments."
	
	Arguments are specific parameters that we can set when we
	call a function, and they're super versatile.
"""

def encode_string(character_offset):
	string_to_encode = input("Please enter a message to encode! [ PRESS ENTER TO ENCODE ] :")
	string_to_encode = string_to_encode.upper()
	output_string = ""
	no_translate = "., ?!"
	#	We don't need the following line, because we've defined it as an argument.
	#character_offset = 6
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
	

print("Welcome to our second Caesar Cipher script")
print("Let's call our first argumented function!")

#	Those parentheses might make a little more sense now...
	

encode_string(3)
encode_string(18)
encode_string(1)
#	Notice that we can now specify an offset of zero, which doesn't encode at all!
encode_string(0)

