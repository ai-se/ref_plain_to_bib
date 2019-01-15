from __future__ import print_function, division
import sys
from pdb import set_trace
from scholar import main
import pandas as pd
import re

def onlyLN(input):
    return re.sub(r"[^a-zA-Z0-9]", "", input)

sheet = pd.read_csv("test_prior.csv")
n = len(sheet)

with open("./out.txt", 'r') as f:
    out = f.read().split("\n\n\n")



newout = []
for i in xrange(n):
    id = i
    tmp = out[i]
    tmpp = tmp.split("\n")
    if i!=int(tmpp[0]):
        print("mismatch")
        exit()
    tmpp[1] = tmpp[1][:tmpp[1].find("{")+1]+tmpp[0]+","
    newstr = "\n".join(tmpp[1:])
    try:
        begin = tmp.find("title={")+len("title={")
        end = tmp.find("}",begin)
        title2 = tmp[begin:end]
    except:
        set_trace()

    title = sheet['Document Title'][i]
    if onlyLN(title.lower()) == onlyLN(title2.lower()):
        newout.append(newstr)
    else:
        newout.append("Mismatch\n"+newstr)

with open("./out_validate.txt", 'w') as f:
    f.write("\n\n\n".join(newout))


