import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import pandas as pd
import numpy as np
from model.seoul_police import Seoulpolice
import matplotlib.pyplot as plt

class SeoulCrimeMap:
    def __init__(self):
        print(f'####baseurl: {baseurl}')
        self.fileReader = FileReader()

    def hook_process(self):
        pass
    
    def get_police_norm(self):
        police = Seoulpolice()
        police_norm = police.get_police_norm()
        return police_norm

    def create_seoul_crime_map(self):
        pass
