
from constants import alphabet

def default_freq_matrix():

    default_matrix = {}

    for letter1 in alphabet:

        sub_dict = {}

        for letter2 in alphabet:
            sub_dict[letter2] = 0
    
        default_matrix[letter1] = sub_dict
    return default_matrix
    

class Bigram_Table:

    def __init__(self, text):

        text = text.lower()

        self.matrix = self.bigramize(text)

        self.key = self.init_key()
    
    def __str__(self):
        return self.key

    def init_key(self):
        key = {}
        for letter in alphabet:
            key[letter] = letter
        
        return key

    def bigramize(self, text):

        matrix = default_freq_matrix()

        total = len(text) - 1

        print(total)

        for i in range(total):
            ch1 = text[i]
            ch2 = text[i + 1]

            ch1 = " " if ch1 == "\n" else ch1
            ch2 = " " if ch2 == "\n" else ch2

            matrix[ch1][ch2] += (1 / total)

        return matrix

    def get_freq(self, bigram):
        bigram = bigram.lower()
        ch1 = bigram[0]
        ch2 = bigram[1]
        return self.matrix[ch1][ch2]

    def swap(self, key1, key2):

        dict1 = self.matrix[key1]
        dict2 = self.matrix[key2]
        
        for key in dict1.items():
            dict1[key], dict2[key] = dict2[key], dict1[key]
        
        for dicts in self.matrix.values():
            dicts[key1], dicts[key2] = dicts[key2], dicts[key1]

                


                    


