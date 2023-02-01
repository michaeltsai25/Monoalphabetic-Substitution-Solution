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
    with open("plaintexts.txt", 'r') as new_file:
        pt = str(new_file.read())
    ptl = str_to_list_2(pt)
    with open("Trainingdata.txt", "w") as data:
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
 
if __name__ == "__main__":
    print(generate_key())