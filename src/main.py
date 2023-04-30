from pathlib import Path
from bigram_table import Bigram_Table
import algorithms

def main():

    ciphertext = text_from_txt("ciphertext.txt")
    training = text_from_txt("training.txt")

    cipher_table = Bigram_Table(ciphertext)

    training_table = Bigram_Table(training)

    print("Eval:", evaluate(training_table, cipher_table))

    print("Decrypted:", decrypt(ciphertext, cipher_table.key))

    print("Swapped.")
    cipher_table.swap("a", "f")

    print("Eval:", evaluate(training_table, cipher_table))

    print("Decrypted:", decrypt(ciphertext, cipher_table.key))

    #algorithms.better_neighbor(cipher_table, training_table, ciphertext)
    algorithms.best_neighbor(cipher_table, training_table, ciphertext)

    print()

    print("Decrypted:", decrypt(ciphertext, cipher_table.key))
    print("Eval:", evaluate(training_table, cipher_table))

    #this is a test comment



def decrypt(text, key):

    decrypted = ""

    for ch in text.lower():
        if ch == "\n":
            decrypted += "\n"
        else:
            decrypted += key[ch]
    
    return decrypted


def evaluate(table1, table2):
    sum = 0
    for dict_key in table1.matrix:
        dict1 = table1.matrix[dict_key]
        dict2 = table2.matrix[dict_key]
        for key in dict1:
            difference = abs(dict1[key] - dict2[key])
            sum += difference
    return sum


def text_from_txt(filename):
    
    src_folder = Path(__file__).parent.absolute()
    repo_root = src_folder.parent.absolute()
    
    string_path = repo_root.as_posix() + "\\Text\\" + filename
    file = open(string_path, "r")
    text = file.read()
    
    return text



if __name__ == "__main__":
    main()
    