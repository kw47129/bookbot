def get_num_words(text):
    """Return the number of words in the text."""
    words = len(text.split())
    return words

def create_dictionary(text):
    lower = text.lower()
    chars = list(lower)
    dict = {}
    for char in chars:
       dict[char] = dict.get(char, 0) + 1
    return dict

def sort_on(items):
    return items["num"]