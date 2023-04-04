import os

def calcFreq(ciphText):
    """Orders the characters in the text from least common to most common"""
    freq = store_freq(ciphText)
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

def store_freq(ciphText):
    """Helper function for calcFreq"""
    text = "".join(set(ciphText))
    freq = {}
    for char in text:
        freq[char] = ciphText.count(char)/len(ciphText)
    return freq

def read_data(name):
    with open(os.path.join("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/Data/", name), 'r') as new_file:
        data = new_file.read()
        data = data.replace('[', "")
        data = data.replace(']', "")
        data = data.split(", ")
        data = [float(point) for point in data]
    return data

def read_dictionary():
    return read_file("dictionary.txt")

def read_plaintext():
    return read_file("TrainingData/TheHungerGames.txt")

def read_file(file):
    """Helper function for read_dictionary and read_plaintext"""
    with open(file, 'r') as new_file:
        dic = new_file.read()
        dic = dic.split('\n')
    return dic

if __name__ == "__main__":
    pass