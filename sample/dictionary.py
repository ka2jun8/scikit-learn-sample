import os
from gensim import corpora

PATH = "./tmp/dictionary.txt"

def is_exist_dictionary():
    if os.path.exists(PATH):
        return True
    else:
        return False

def get_dictionary(words, updateFlag = False):
    dictionary = None
    if is_exist_dictionary() and updateFlag == False:
        dictionary = corpora.Dictionary.load_from_text(PATH)
    else:
        dictionary = corpora.Dictionary(words)
        dictionary.save_as_text(PATH)
    dictionary.filter_extremes(no_below = 200, no_above = 0.2)
    return dictionary
