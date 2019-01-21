from __future__ import print_function, division
import sys
from pdb import set_trace
from scholar import main
import pandas as pd
import time
import random

import urllib2

def download_file(download_url,id):
    response = urllib2.urlopen(download_url)
    file = open("./pdf/"+str(id)+".pdf", 'w')
    file.write(response.read())
    file.close()

sheet = pd.read_csv("test_prior.csv")
n = len(sheet)


orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

for i in xrange(n):
    id = i
    title = sheet['Document Title'][i]
    if title=='':
        continue
    print(id)
    sys.argv= ['-c' , '1', '--phrase', title, '--citation',  'bt', '-t']
    main()
    # if sheet['PDF Link'][i]:
    #     download_file(sheet['PDF Link'][i],id)

    time.sleep(10)


f.close()
sys.stdout = orig_stdout

