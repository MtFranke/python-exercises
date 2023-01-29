# Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

# Twinkle, twinkle, little star,
#	How I wonder what you are!
#		Up above the world so high,
#		Like a diamond in the sky.
# Twinkle, twinkle, little star,
#	How I wonder what you are

def printer(text, amount_of_white_spaces):
    indent = len(text) + amount_of_white_spaces
    formatted_text = text.rjust(indent, " ")
    print(formatted_text)


printer("Twinkle, twinkle, little star,", 0)
printer("How I wonder what you are!", 4)
printer("Up above the world so high.", 8)
printer("Like a diamond in the sky.", 8)
printer("Twinkle, twinkle, little star,", 0)
printer("How I wonder what you are,", 4)
