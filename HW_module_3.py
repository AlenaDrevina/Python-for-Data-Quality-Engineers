import re
import string

message = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Last words of each existing sentence (whitespace+word+dot)
find_all_last_word = re.findall(r'\s(\w+)?\.', message)

variable = find_all_last_word[0]
view = find_all_last_word[1]
paragraph = find_all_last_word[2]
here = find_all_last_word[3]
mistake = find_all_last_word[4]
text = find_all_last_word[5]
whitespaces = find_all_last_word[6]
number_87 = find_all_last_word[7]

# One more sentence with last words of each existing sentence
new_sentence = f'\t{variable}, {view}, {paragraph}, {here}, {mistake}, {text}, {whitespaces}, {number_87}.\n'

# Adding new sentence to the end of this paragraph
full_text = message + new_sentence

# split message by sentences (by dot)
normalized = re.split('(\.\s+)', full_text)

# Capitalize first letters of each sentence
capital_letters = [i.capitalize() for i in normalized]

# Union back into single message
capitalized_message = ''.join(capital_letters)

# Replacing iz by is in necessary
misspelling = capitalized_message.replace(' iz', ' is')
print(f'Corrected homework:\n{misspelling}')

# Calculate number of whitespace characters in this text
count_whitespace = list(s for s in misspelling if s.isspace())
print(f'Number of whitespaces: {len(count_whitespace)}')