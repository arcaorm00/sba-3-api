import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_helper import FileReader
import pandas as pd
import numpy as np

class Seoulcrime:
    
    def __init__(self):
        self.fileReader = FileReader()
        self.context = '/Users/saltQ/sba-3-api/model/data/'

    def fileinfo(self):
        crimeFile = 'crime_in_seoul.csv'

        this = self.fileReader
        this.context = self.context
        this.fname = crimeFile
        return pd.read_csv(this.context + this.fname)


if __name__ == '__main__':
    sc = Seoulcrime()
    print(sc.fileinfo())
    