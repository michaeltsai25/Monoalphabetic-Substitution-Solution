import numpy as np

def org_bigrams():
    with open("Data/Bigrams_org/bigramsfreq.txt", "r") as file:
        bi=file.read()
        bi=bi.split("\n")
        tot_list=[]
        inner_list=[]
        for line in bi:
            count=0
            for idx, char in enumerate(line):
                if char==" ":
                    count+=1
                    if count%2==1:
                        inner_list.append(line[idx+1:idx+6])
            tot_list.append(inner_list.copy())
            inner_list.clear()
    return tot_list