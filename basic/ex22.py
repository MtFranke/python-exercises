"""
Write a Python program to count the number 4 in a given list
"""

collection_of_numbers = [1, 2, 4, 4, 5, 1, 2, 4]
number_of_occurrence = 0
search_number = 4

for n in collection_of_numbers:
    if n == search_number:
        number_of_occurrence += 1

print(f"number of of occurrence number {search_number} in {collection_of_numbers} is -> {number_of_occurrence}")
