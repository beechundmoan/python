"""
	What if we don't want to immediately print the output of our function?
	
	What if, for example, we want to store the encoded message in a variable
	for later use or further processing?
	
	Instead of using the print() function, we'll use the RETURN keyword.
	All functions return a value of some kind, but it's not printed to the
	screen unless it's told to. 
	
	(Some builtin functions, like print(), pretend to not return a value)
"""

def encode_string(character_offset):
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
	#	Here's the change:
	return(output_string)
	

print("Welcome to our third Caesar Cipher script")
print("Are you feeling educated yet?")

our_encoded_string = encode_string(4)

print("Your message is now stored in a variable!")

#	does this format look familiar now?
should_we_print_message = input("Would you like to read your encoded message? [y/n]:")	

if should_we_print_message is "y":
	print(our_encoded_string)
else:
	print("Fine, be like that.")