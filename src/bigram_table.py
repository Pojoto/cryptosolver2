
import constants
    
class Bigram_Table:

    def __init__(self, text):

        text = text.upper()

        self.matrix = self.bigramize(text)

        key = {}
        self.init_key(key)

        self.key = key
    
    def __str__(self):
        return self.key

    
    def init_key(self, key):
        for letter in constants.alphabet:
            key[letter] = letter
        
        #return key

    def bigramize(self, text):

        matrix = constants.default_freq_matrix

        for i in range(len(text) - 1):
            ch1 = text[i]
            ch2 = text[i + 1]
            matrix[ch1][ch2] += 1
        
        return matrix

    def swap(self, i1, j1, i2, j2):
        
        pass


