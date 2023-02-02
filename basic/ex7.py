# Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
# Sample filename : abc.java
# Output : java

user_input = input("Provide filename to determine extension of that file: ")
file_extension = list(user_input.split('.'))
file_extension.reverse()
print(file_extension[0])
