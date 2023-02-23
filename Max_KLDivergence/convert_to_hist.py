import matplotlib.pyplot as plt
import numpy as np
import os

def convert():
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/Data/data.txt", 'r') as new_file:
        data = new_file.read()
        data = data.replace('[', "")
        data = data.replace(']', "")
        data = data.split(", ")
        data = [float(point) for point in data]
        data = np.array(data)
        plt.hist(data)
        my_path = "/Users/michaeltsai/Documents/GitHub/Monoalphabetic-Substitution-Solution"
        plt.savefig(my_path + "/Data/Distr.png")

def save_plot(data):
    pass

if __name__ == "__main__":
    convert()