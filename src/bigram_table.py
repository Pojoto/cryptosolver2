
from constants import alphabet
    
class bigram_table:

    def __init__(self, text):

        self.matrix = bigramize(text)

        key = {}
        init_key(key)

        self.key = key

    
    def init_key(key):
        for letter in alphabet:
            key[letter] = letter
        
        #return key

    def bigramize(text):

        matrix = [[0]]

        return matrix

