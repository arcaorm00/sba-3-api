import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import pandas as pd
import numpy as np

class Seoulcrime:

    def __init__(self):
        self.fileReader = FileReader()

    def get_crime(self):
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'crime_in_seoul.csv'
        crimeFile = reader.csv_to_dframe()
        print(crimeFile)

if __name__ == '__main__':
    model = Seoulcrime()
    model.get_crime()
    