from __future__ import print_function, division
import sys
import numpy as np
from pdb import set_trace
from scholar import main

with open("ref", "r") as f:
    content = str(unicode(f.read(), errors='ignore'))

x = np.array(content.split('"'))
y = np.array(range(int(len(x)/2)))*2+1
z = x[y]
z = map(str.strip, z)

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

for i,title in enumerate(z):
    print('%% [%d]' %(i+1))
    sys.argv= ["" , '-c' , '1', '--phrase', title, '--citation',  'bt']
    main()

f.close()
sys.stdout = orig_stdout

