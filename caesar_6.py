"""
	Now we have a very functional script that will take an (uppercase) input string
	and encrypt it with a basic Caesar cipher, but we can do some things
	to tidy it up and make it more readable. 
	
	I've removed my previous comments to make it easier to highlight the new changes
	
"""


string_to_encode = "HELLO WIGGLES, HOW ARE YOU?"

output_string = ""

no_translate = "., ?!" 

character_offset = 6

for character in string_to_encode:
	if character in no_translate:
		"""
			DRY: Don't Repeat Yourself!
			
			We already have a line that adds our character to our output
			string, so let's avoid retyping it!
			
			Note that, if we were to use the CONTINUE keyword here,
			the script would *only* handle our punctuation characters,
			and ignore the rest.
			
			Instead, we'll use an ELSE statement to handle where our IF condition
			is false.
		"""
		new_character = character
	else:
		ascii_code = ord(character)

		new_ascii_code = ascii_code + character_offset

		if new_ascii_code > 90:
			#	The following is a much shorter way of writing new_ascii_code = new_ascii_code - 25
			new_ascii_code -= 25

		new_character = chr(new_ascii_code)
	#	The following is a much shorter way of writing output_string = output_string + new_character ... look familiar?
	output_string += new_character

print(output_string)