from pathlib import Path
from bigram_table import Bigram_Table

def main():

    ciphertext = text_from_txt("ciphertext.txt")
    training = text_from_txt("training.txt")

    cipher_table = Bigram_Table(ciphertext)

    print(cipher_table.matrix)

    print(cipher_table.matrix["T"]["H"])
    print(cipher_table.matrix["L"]["K"])

    print(ciphertext)
    print(training)


    #this is a test comment








def text_from_txt(filename):
    
    src_folder = Path(__file__).parent.absolute()
    repo_root = src_folder.parent.absolute()
    
    string_path = repo_root.as_posix() + "\\Text\\" + filename
    file = open(string_path, "r")
    text = file.read()
    
    return text



if __name__ == "__main__":
    main()
    