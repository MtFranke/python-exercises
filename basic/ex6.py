# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

user_numbers = input("Please enter sequence of comma-separated numbers: ")

user_numbers_list = user_numbers.split(',')
user_numbers_tuple = tuple(user_numbers_list)

print(user_numbers_list)
print(user_numbers_tuple)
