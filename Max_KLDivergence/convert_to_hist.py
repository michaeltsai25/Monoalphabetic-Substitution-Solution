import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
import sys
sys.path.append("./Code/Env")
from utils import read_data

def convert(img_name, txt_name, hist):
    data = read_data(txt_name)
    data = np.array(data)
    if hist:
        plt.hist(data)
    else:
        sns.set_style('whitegrid')
        sns.kdeplot(data, bw=0.5)
    my_path = "/Users/michaeltsai/Documents/GitHub/Monoalphabetic-Substitution-Solution"
    plt.savefig(os.path.join(my_path + "/Data/" + img_name))
    plt.show()

if __name__ == "__main__":
    convert("Samp_Distr.png", "Samp_Distr.txt", False)