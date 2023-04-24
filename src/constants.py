
alphabet = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

default_freq_matrix = {}

for letter1 in alphabet:

    sub_dict = {}

    for letter2 in alphabet:
        sub_dict[letter2] = 0
    
    default_freq_matrix[letter1] = sub_dict

