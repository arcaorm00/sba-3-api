import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import pandas as pd
import numpy as np
from sklearn import preprocessing

from model.seoul_crime import Seoulcrime

'''
Index(['Unnamed: 0', '관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생',
       '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거', '구별'],
      dtype='object')
'''

class Seoulpolice:

    def __init__(self):
        self.fileReader = FileReader()

    def hook_process(self):
        print('--------------- POLICE ---------------')
        self.create_crime_rate()
    
    def create_crime_rate(self):
        crime = Seoulcrime()
        crime_police = crime.get_crime_police()
        police = pd.pivot_table(crime_police, index='구별', aggfunc=np.sum)
        print(f'{police.head()}') # 구별로 값을 모두 더함

        police['살인검거율'] = (police['살인 검거']/police['살인 발생']) * 100
        police['강도검거율'] = (police['강도 검거']/police['강도 발생']) * 100
        police['강간검거율'] = (police['강간 검거']/police['강간 발생']) * 100
        police['절도검거율'] = (police['절도 검거']/police['절도 발생']) * 100
        police['폭력검거율'] = (police['폭력 검거']/police['폭력 발생']) * 100

        police.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'}, axis=1)
        crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']

        for i in crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100 # 데이터 값의 기간오류 탓에 확률이 100이 넘으면 100으로 계산

        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        crime_columns = ['살인', '강도', '강간', '절도', '폭력']

        x = police[crime_rate_columns].values
        min_max_scaler = preprocessing.MinMaxScaler()

if __name__ == '__main__':
    police = Seoulpolice()
    police.hook_process()
    

