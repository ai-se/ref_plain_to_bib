from __future__ import print_function, division
import sys
from pdb import set_trace
from scholar import main
import pandas as pd

import requests



def download_file(download_url,id):
    chunk_size = 2000
    r = requests.get(download_url, stream=True)
    set_trace()
    file = open("./pdf/"+str(id)+".pdf", 'wb')
    for chunk in r.iter_content(chunk_size):
        file.write(chunk)
    file.close()

download_file("https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8326489",01)


