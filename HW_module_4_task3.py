import re

# function which corrects text format
def text_decomposition_for_correctness(message):
    text = message.lower()                            # converts a message into lower case
    splitted = re.split('(\.\s+)', text)              # split text on sentence
    capital_letters = [word.capitalize() for word in splitted]  # capitalize first letters of each sentence
    capital_letters_join = "".join(capital_letters)            # union all parts
    misspelling = capital_letters_join.replace(' iz', ' is')   # replace 'iz' by 'is'
    return misspelling

# function which returns last word and create new sentence
def create_sentence_with_the_last_words(message):
    find_all_last_word = re.findall(r"\s(\w+)\.\s+", text_decomposition_for_correctness(message))  # find all last words
    all_words = ', '.join(find_all_last_word).lower().capitalize()           # union them
    sentence = f'\t{all_words}.\n'  # create new sentence
    return sentence

# function which unions correct text and sentence that contains last words
def create_text_consist_of_old_text_with_new_sentence(message):
    text = text_decomposition_for_correctness(message) + create_sentence_with_the_last_words(message)
    return text

#count the whitespaces
def count_filtered_whitespaces(message):
    return len(list(s for s in message if s.isspace()))

# Text variable
message = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

print(f'Corrected mistakes:\n', create_text_consist_of_old_text_with_new_sentence(message))
print(f'Number of whitespaces: {count_filtered_whitespaces(message)}')
