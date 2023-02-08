from math import log

def kl_divergence(cipherDistr, plainDistr):
    div = 0
    for i in range(26):
        div += cipherDistr[i]*log(cipherDistr[i]/plainDistr[i])
    return div

def calcFreq(ciphText):
    ciphText = ciphText.replace(" ", "")
    text = "".join(set(ciphText))
    freq = {}
    for char in text: 
        freq[char] = ciphText.count(char)/len(ciphText)
    return sorted(freq.items(), key=lambda x: x[1])

if __name__ == "__main__":
    print(calcFreq("this is a test"))