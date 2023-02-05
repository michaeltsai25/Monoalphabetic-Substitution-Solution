from math import log

def kl_divergence(cipherDistr, plainDistr):
    div = 0
    for i in range(26):
        div += cipherDistr[i]*log(cipherDistr[i]/plainDistr[i])
    return div