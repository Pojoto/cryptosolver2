from constants import alphabet


def evaluate(table1, table2):
    sum = 0
    for dict_key in table1.matrix:
        dict1 = table1.matrix[dict_key]
        dict2 = table2.matrix[dict_key]
        for key in dict1:
            difference = abs(dict1[key] - dict2[key])
            sum += difference
    return sum

def decrypt(text, key):

    decrypted = ""

    for ch in text.lower():
        if ch == "\n":
            decrypted += "\n"
        else:
            decrypted += key[ch]
    
    return decrypted



def better_neighbor(bigram_table, training_table, ciphertext):
    
    i = 0

    while i < len(alphabet):

        j = 0

        while j < len(alphabet):

            current_eval = evaluate(bigram_table, training_table)
            
            letter1 = alphabet[i]
            letter2 = alphabet[j]

            bigram_table.swap(letter1, letter2)

            if evaluate(bigram_table, training_table) >= current_eval:
                bigram_table.swap(letter1, letter2)
            else:
                print(f"Swapped {letter1} and {letter2}.")
                print(decrypt(ciphertext, bigram_table.key))
                i = 0
                j = 0

            j += 1

        i += 1

def best_neighbor(bigram_table, training_table, ciphertext):

    i = 0

    while i < len(alphabet):

        j = 0

        best  = evaluate(bigram_table, training_table)
        swap1, swap2 = 0, 0

        while j < len(alphabet):

            current_eval = evaluate(bigram_table, training_table)
            
            letter1 = alphabet[i]
            letter2 = alphabet[j]

            bigram_table.swap(letter1, letter2)

            swapped_eval = evaluate(bigram_table, training_table)

            if swapped_eval < current_eval:
                print("found better", swap1, swap2)
                best = swapped_eval
                swap1 = letter1
                swap2 = letter2

            j += 1
        
        if swap1 != 0 and swap2 != 0:
            bigram_table.swap(letter1, letter2)
            #print(f"Swapped {letter1} and {letter2}.")
            #print(decrypt(ciphertext, bigram_table.key))
            i = 0

        i += 1