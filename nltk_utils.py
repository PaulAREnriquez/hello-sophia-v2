import nltk
#nltk.download('punkt') # remember to download this
from nltk.stem import WordNetLemmatizer
import numpy as np
"""
Python file containing functions to implement:

1. tokenization
2. Lemmatization
3. bag of words

"""


lemmatizer = WordNetLemmatizer()

def tokenize(sentence):
    
    return nltk.word_tokenize(sentence)

def lemma(word):
    return lemmatizer.lemmatize(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    tokenized_sentence = ['hello', 'how', 'are', 'you']
    words = ['hi', 'hello','i', 'how', 'are','you', 'bye','thank', 'cool']
    bag = [0, 1, 0, 1, 1, 1, 0, 0, 0]

    if the tokenized_sentence contains words not in the words, it will be ignored.
    say: using the same words list as above
    tokenized_sentence = ['hello', 'how', 'are', 'you', 'good','morning']
    bag = [0, 1, 0, 1, 1, 1, 0, 0, 0] # the 0,0,0 at the end is for 'bye', 'thank', 'cool

    """
    tokenized_sentence = [lemma(word) for word in tokenized_sentence]

    bag = np.zeros(len(all_words))

    for idx, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[idx] = 1.0

    return bag
