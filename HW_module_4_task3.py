import re

# Text variable
message = """homEwork:
	tHis iz your homeWork, copy these Text to variable.
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Last words of each existing sentence
def find_all_last_word(a, b):
    return re.findall(a, b)


# Additional activities concerns with normalization of our text
def splitted(a):
    text = message + ', '.join(find_all_last_word)
    splitted = re.split(a, text)
    capital_letters = [i.capitalize() for i in splitted]
    return ''.join(capital_letters)

# Replace iz by is if necessary
def misspelling(a, b):
    return splitted.replace(a, b)

# Calculate number of whitespace characters in this text
def filtered_whitesp():
    return len(list(s for s in misspelling if s.isspace()))

find_all_last_word = find_all_last_word('\s(\w+)?\.', message)

splitted = splitted('(\.\s+)')

misspelling = misspelling(" iz", " is")
print(f'Corrected mistakes:\n{misspelling}')

print(f'Number of whitespaces: {filtered_whitesp()}')
