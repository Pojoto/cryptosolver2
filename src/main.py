from pathlib import Path
from bigram_table import Bigram_Table

def main():

    ciphertext = text_from_txt("ciphertext.txt")
    training = text_from_txt("training.txt")

    cipher_table = Bigram_Table(ciphertext)

    training_table = Bigram_Table(training)

    # print(training_table.matrix)

    print(cipher_table.matrix)

    print(cipher_table.get_freq("TH"))
    print(cipher_table.get_freq("LK"))
    print(cipher_table.get_freq("ZZ"))
    print(cipher_table.get_freq("ZQ"))

    print()

    print(training_table.get_freq("TH"))
    print(training_table.get_freq(" t"))
    print(training_table.get_freq("lk"))
    print(training_table.get_freq("zq"))
    print(training_table.get_freq("zz"))

    print("Eval:", evaluate(training_table, cipher_table))

    #this is a test comment





def evaluate(table1, table2):
    sum = 0
    for dict_key in table1.matrix:
        dict1 = table1.matrix[dict_key]
        dict2 = table2.matrix[dict_key]
        for key in dict1:
            difference = (dict1[key] - dict2[key]) ** 2
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
    