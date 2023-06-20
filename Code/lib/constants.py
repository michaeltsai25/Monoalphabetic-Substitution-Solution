import sys
sys.path.append("./Data/Bigrams_org")
from org import org_bigrams
import numpy as np
MAX_KL_DIV = 0.3
DISTR_ENG_LETTERS = [0.127020, 0.090560, 0.081670,  0.075070, 0.069660, 0.067490, 0.063270, 0.060940, 0.059870, 0.042530, 0.040250, 0.027820, 0.027580, 0.024060, 0.023600, 0.022280, 0.020150, 0.019740, 0.019290, 0.014920, 0.009780, 0.007720, 0.001530, 0.001500, 0.000950, 0.000740]
BIGRAMS_DISTR = np.array(org_bigrams())
ALPH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
MAX_ITER = 1000 #change this once figured out
MIN_WORDS = 10 #change this once figured out