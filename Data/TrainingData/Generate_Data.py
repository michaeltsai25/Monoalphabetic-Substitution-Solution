import string
from random import randint
import sys
sys.path.append("./Code/lib")
from utils import read_plaintext

def encrypt_plaintext(key, plaintext):
    """Takes in a string key and plaintext and encrypts the plaintext with the key"""
    ciph_text = ""
    l_plaintext = str_to_list(plaintext.lower())
    for item in l_plaintext:
        ciph_text += key[item]
    return ciph_text

def str_to_list(string):
    """Helper function for encrypt_plaintext. Converts a certain string and converts it to a list containing each character in the string (exluding spaces)."""
    chars = []
    for char in string: 
        if char == ' ':
            continue
        chars.append(char)
    return chars

def generate_key():
    """Generates random keys"""
    key = {}
    alph = string.ascii_lowercase
    for i in range(26):
        ch = alph[randint(0, 25-i)]
        key.update({string.ascii_lowercase[i]: ch})
        alph = alph.replace(ch, '')
    return key

def encrypt_text_file():
    """Encrypts text files with random keys"""
    ptl = read_plaintext()
    with open("Data/TrainingData/trainingdata.txt", "w") as data:
        for item in ptl:
            key = generate_key()
            data.write(item + "\n")
            data.write(encrypt_plaintext(key, item))
            data.write(f"\n{key}\n\n")

def convert_plaintexts(no_spaces, name):
    hg = ""
    with open(f"/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/TrainingData/{name}", 'r') as new_file:
        hg = new_file.read()
        hg = hg.lower()
        if no_spaces == True:
            hg = "".join(hg.split())
        count = 0
        length = len(hg)
        for i in range(len(hg)):
            if i-count > 28 and hg[i] in string.punctuation:
                ss1 = hg[0:i]
                ss2 = hg[i+1:length]
                hg = ss1+'\n'+ss2
                count = i
        hg = hg.translate(str.maketrans('', '', string.punctuation))
    with open(f"/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/TrainingData/{name}", "w") as new_file:
        new_file.write(hg)

"""
def prep_dict():
    Removes one character words from the dictionary
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/dictionary.txt", 'r') as new_file:
        words = new_file.read()
        words = words.split("\n")
        for word in words:
            if len(word) == 1:
                words.remove(word)
    file = ""
    for word in words:
        file += word
        file += '\n'
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/dictionary.txt", 'w') as new_file:
        new_file.write(file)
"""

def exclude_unc_words():
    with open("TrainingData/HungerGamesTest.txt", 'r') as new_file:
        hg = new_file.read()
    with open("dictionary.txt", 'r') as new_file: 
        dic = new_file.read()
        dic = dic.split('\n')
    com_words = ""
    for word in dic:
        if word in hg:
            com_words += word
            com_words += '\n'
    with open("com_word_dic.txt", 'w') as new_file:
        new_file.write(com_words)

def prep_dict():
    with open("/Users/michaeltsai/Documents/GitHub/Monoalphabetic-Substitution-Solution/com_word_dic.txt", 'r') as new_file:
        dic = new_file.read()
        dic = dic.split("\n")
    for i in  range(len(dic)):
        for j in range(i+1, len(dic)): #doesn't work, but eventually edits the file if it is run enough times
            try:
                if dic[i] in dic[j]:
                    dic.remove(dic[i])
            except IndexError:
                print(f"i={i}")
                print(f"j={j}")
    str_dic = ""
    for word in dic:
        str_dic += word
        str_dic += "\n"
    with open("/Users/michaeltsai/Documents/GitHub/Monoalphabetic-Substitution-Solution/com_word_dic.txt", 'w') as new_file:
        new_file.write(str_dic)

def rem_one_letter_chars():
    with open("/Users/michaeltsai/Documents/GitHub/Monoalphabetic-Substitution-Solution/com_word_dic.txt", 'r') as new_file:
        dic = new_file.read()
        dic = dic.split("\n")
    for char in dic:
        if len(char) == 1:
            dic.remove(char)
    str_dic = ""
    for word in dic:
        str_dic += word
        str_dic += "\n"
    with open("com_word_dic.txt", 'w') as new_file:
        new_file.write(str_dic)

def clean_pt():
    pt = read_plaintext()
    for i in range(len(pt)):
        for char in "0123456789":
            if char in pt[i]:
                pt[i] = pt[i].replace(char, "")
    data = ""
    for text in pt:
        data += text
        data += "\n"
    with open("TrainingData/TheHungerGames.txt", 'w') as new_file:
        new_file.write(data)

def increase_training_data_len():
    file = read_plaintext()
    total = ""
    current = ""
    for i in range(len(file)):
        if i%3 == 0:
            total += current + "\n"
            current = ""
        current += file[i]
        i += 1
    with open("Data/TrainingData/TheHungerGames.txt", "w") as new_file:
        new_file.write(total)

if __name__ == "__main__":
    #convert_plaintexts(False, "HungerGamesTest.txt")
    encrypt_text_file()
    #increase_training_data_len()