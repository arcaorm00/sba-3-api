import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import pandas as pd
import numpy as np
from sklearn import preprocessing

from model.seoul_crime import Seoulcrime
from model.seoul_cctv import Seoulcctv

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
        self.set_police_norm()
        print(self.get_police_norm().head())
    
    def set_police_norm(self):
        crime = Seoulcrime()
        crime_police = crime.get_crime_police()
        police = pd.pivot_table(crime_police, index='구별', aggfunc=np.sum)
        print(f'{police.head()}') # 같은 구에 해당하는 값을 모두 더함

        police['살인검거율'] = (police['살인 검거']/police['살인 발생']) * 100
        police['강도검거율'] = (police['강도 검거']/police['강도 발생']) * 100
        police['강간검거율'] = (police['강간 검거']/police['강간 발생']) * 100
        police['절도검거율'] = (police['절도 검거']/police['절도 발생']) * 100
        police['폭력검거율'] = (police['폭력 검거']/police['폭력 발생']) * 100

        police.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'}, axis=1)
        crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']

        for i in crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100 # 데이터 값의 기간오류 탓에 확률이 100이 넘으면 100으로 변경

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
        # 스케일: 대수를 표준화 시키기 위함 (평균 0 분산 1)
        # 스케일링은 선형변환을 적응하여 전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        x_scaled = min_max_scaler.fit_transform(x.astype(float)) 
        # 연속형 자료형으로 만들기 위함. 왜? 정규 분포를 그려야 하니까. 왜? 회귀니까!
        '''
        정규화(normalization)
        많은 양의 데이터를 처리함에 있어 여러 이유로 정규화, 즉 데이터의 범위를 일치시키거나
        분포를 유사하게 만들어 주는 등의 작업. 평균값 정규화, 중간값 정규화 등...
        '''
        police_norm = pd.DataFrame(x_scaled, columns=crime_columns, index=police.index)
        police_norm[crime_rate_columns] = police[crime_rate_columns]

        cctv = Seoulcctv()
        cctv_pop = cctv.get_cctv_pop()
        print(f'cctv_pop: {cctv_pop.head()}')

        police_norm['범죄'] = np.sum(police_norm[crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[crime_columns], axis=1)
        print(f'price_norm columns: {police_norm.columns}')

        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'saved_data')
        reader.fname = 'police_norm.csv'
        police_norm.to_csv(reader.new_file(), sep=',', encoding='UTF-8')

    def get_police_norm(self):
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'saved_data')
        reader.fname = 'police_norm.csv'
        police_norm = pd.read_csv(os.path.join(reader.context, reader.fname))
        return police_norm

if __name__ == '__main__':
    police = Seoulpolice()
    police.hook_process()
    

