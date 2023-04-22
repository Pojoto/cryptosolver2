
from constants import alphabet
    
class bigram_table:

    def __init__(self, text):

        self.matrix = self.bigramize(text)

        key = {}
        self.init_key(key)

        self.key = key
    
    def __str__(self):
        return self.key

    
    def init_key(key):
        for letter in alphabet:
            key[letter] = letter
        
        #return key

    def bigramize(text):

        matrix = [[0]]

        return matrix

