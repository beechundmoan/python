"""
	Our previous scripts all functioned as standalone programs,
	where the whole program is dedicated to one single task.
	
	If we wanted to incorporate that task into a larger program,
	we can "wrap the task into a function." 
	
	Functions are a named block of code that we can call
	whenever we need to do a task that might be repetitive 
	to type out every single time it needs to be done.
			
"""

def encode_string():
	string_to_encode = input("Please enter a message to encode! [ PRESS ENTER TO ENCODE ] :")
	string_to_encode = string_to_encode.upper()
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
	
"""
	At this point in our script, nothing will happen on screen. 
	All we have done is to *define* the function, now it's ready
	to be *called.*
	
"""

print("Welcome to our first Caesar Cipher script")
print("Let's call our first function!")

"""
	Functions need to be called with the parentheses like below,
	otherwise they'll be treated like variables -
	and since we didn't create a variable named encode_string,
	our program won't work properly (or at all).

	The best part of this is that, if we wanted to encode 7 different
	strings in the same way, we only need to call the function
	7 times - rather than typing out the whole instruction list
	each and every time.
	
"""
encode_string()
encode_string()
encode_string()
encode_string()
encode_string()
encode_string()
encode_string()

