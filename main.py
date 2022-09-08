
import spacy

#Loading and using models
# load() with the model name or a path to the model data directory. 
#import spacy nlp =spacy. load("en_core_web_sm")
#doc = nlp("This is a sentence.")
#You can also import a model directly via its full name and then call its #load() method with no arguments.

from keytotext import pipeline


#The data used for training “keytotext” is taken from WebNLG and DART: Open-#Domain Structured Data Record to Text Generation, wherein,
#you get XML or #JSON files containing triples for a given
#sentence from various domains such as #comic character, food, etc.

from collections import Counter

#a container that is used to store collections of data, for example - list, dict, #set, and tuple, etc

from string import punctuation

nlp = spacy.load("en_core_web_sm")

def get_hotwords(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] # 1
    
    doc = nlp(text.lower()) # 2
    for token in doc:
        # 3
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        # 4
        if(token.pos_ in pos_tag):
            result.append(token.text)
    return result # 5
