import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import pandas as pd
import numpy as np

class UsUnemployment:

    def __init__(self):
        self.filereader = FileReader()

    def show_map(self):
        reader = self.filereader
        reader.context = os.path.join(basedir, 'data')
        reader.fname = 'us_unemployment.csv'
        unemployment_data = pd.read_csv(os.path.join(reader.context, reader.fname))
        print(unemployment_data.head())

        
if __name__ == '__main__':
    unemployment = UsUnemployment()
    unemployment.show_map()
    