from math import log

def kl_divergence(cipherDistr, plainDistr):
    """Calculates the Kullback-Leibler Divergence between two distributions"""
    div = 0
    for i in range(26):
        div += cipherDistr[i]*log(cipherDistr[i]/plainDistr[i])
    return div

def calcFreq(ciphText):
    """Orders the characters in the text from least common to most common"""
    ciphText = ciphText.replace(" ", "")
    text = "".join(set(ciphText))
    freq = {}
    for char in text: 
        freq[char] = ciphText.count(char)/len(ciphText)
    return sorted(freq.items(), key=lambda x: x[1])

if __name__ == "__main__":
    print(calcFreq("this is a test"))