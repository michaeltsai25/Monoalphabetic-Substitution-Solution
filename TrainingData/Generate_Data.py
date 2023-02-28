import string
from random import randint

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
    with open("The Hunger Games.txt", 'r') as new_file:
        pt = str(new_file.read())
    ptl = str_to_list_2(pt)
    with open("trainingdata.txt", "w") as data:
        for item in ptl: 
            key = generate_key()
            data.write(encrypt_plaintext(key, item))
            data.write(f"\n{key}\n\n")
    
def str_to_list_2(string):
    l = []
    ss = 0
    for i in range(len(string)):
        if string[i: i+1] == "\n":
            l.append(string[ss:i])
            ss = i+2
    return l

def convert_plaintexts():
    hg = ""
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/TrainingData/TheHungerGames.txt", 'r') as new_file:
        hg = new_file.read()
        hg = "".join(hg.split())
        hg = hg.lower()
        hg.replace(' ', '')
        count = 0
        length = len(hg)
        for i in range(len(hg)):
            if i-count > 28 and hg[i] in string.punctuation:
                ss1 = hg[0:i]
                ss2 = hg[i+1:length]
                hg = ss1+'\n'+ss2
                count = i
        hg = hg.translate(str.maketrans('', '', string.punctuation))
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/TrainingData/TheHungerGames.txt", "w") as new_file:
        new_file.write(hg)

def prep_dict():
    """Removes one character words from the dictionary"""
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
 
if __name__ == "__main__":
    prep_dict()