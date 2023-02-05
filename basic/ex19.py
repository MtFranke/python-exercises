"""
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is".
"""


def check_string(text: str) -> str:
    beginning = text[:2]
    if beginning == 'Is':
        return text
    return "Is" + text


print(f"Is Empty -> {check_string('Is Empty')}")
print(f"IsEmpty -> {check_string('IsEmpty')}")
print(f"Array -> {check_string('Array')}")
