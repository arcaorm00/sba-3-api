import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import pandas as pd
import numpy as np

class Seoulcctv:

    def __init__(self):
        # print(f'basedir: {baseurl}')
        self.fileReader = FileReader()

    def get_cctv(self):
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'cctv_in_seoul.csv'
        cctv = reader.csv_to_dframe()
        print(cctv)
        return cctv

    def get_pop(self):
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'pop_in_seoul.xls'
        pop = reader.xls_to_dframe(2, 'B, D, G, J, N')
        print(pop)
        return pop


if __name__ == '__main__':
    model = Seoulcctv()
    model.get_cctv()
    model.get_pop()


    

    




