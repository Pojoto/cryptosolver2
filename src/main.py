from pathlib import Path


def main():
    print(text_from_txt("ciphertext.txt"))
    print(text_from_txt("training.txt"))
    









def text_from_txt(filename):
    
    src_folder = Path(__file__).parent.absolute()
    repo_root = src_folder.parent.absolute()
    
    string_path = repo_root.as_posix() + "\\Text\\" + filename
    file = open(string_path, "r")
    text = file.read()
    
    return text



if __name__ == "__main__":
    main()
    