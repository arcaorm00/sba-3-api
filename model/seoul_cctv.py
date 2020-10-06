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

    def hook_process(self): # hook 메소드: 처리 순서
        print('--------------- CCTV & POP ---------------')
        cctv = self.get_cctv()
        pop = self.get_pop()
        print(f'CCTV Header: \n{cctv.head()}')
        print(f'POP Header: \n{pop.head()}')
        self.set_cctv_pop(pop, cctv)
        

    def get_cctv(self):
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'cctv_in_seoul.csv'
        cctv = reader.csv_to_dframe()
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace = True)
        # print(cctv)
        return cctv

    def get_pop(self):
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'data')
        reader.fname = 'pop_in_seoul.xls'
        pop = reader.xls_to_dframe(2, 'B, D, G, J, N')
        pop.rename(columns={
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자'
            }, inplace = True)
        print(f"POP Null Check: {pop['구별'].isnull()}")
        pop.drop([26], inplace=True) # inplace: 원본에서 삭제한다.
        # print(pop)
        return pop

    """
        고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                    [-0.28078554  1.        ]] 
        외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                    [-0.13607433  1.        ]]
       r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
       r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
       r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
       r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
       r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
       r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
       r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
       고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                   [-0.28078554  1.        ]]
       외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                   [-0.13607433  1.        ]]                        
    """ 

    def set_cctv_pop(self, pop, cctv):
        pop['외국인비율'] = pop['외국인'] / pop['인구수'] * 100
        pop['고령자비율'] = pop['고령자'] / pop['인구수'] * 100
        cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'], 1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on='구별')
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])

        print(f'고령자 비율과 CCTV의 상관계수는 {cor1}')
        print(f'외국인 비율과 CCTV의 상관계수는 {cor2}')
        '''
        고령자 비율과 CCTV의 상관계수는 [[ 1.         -0.28078554] 약한 음적 선형관계
        [-0.28078554  1.        ]]
        외국인 비율과 CCTV의 상관계수는 [[ 1.         -0.13607433] 거의 무시될 수 있는 선형관계
        [-0.13607433  1.        ]]
        '''
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'saved_data')
        reader.fname = 'cctv_pop.csv'
        cctv_pop.to_csv(reader.new_file())

    def get_cctv_pop(self):
        reader = self.fileReader
        reader.context = os.path.join(baseurl, 'saved_data')
        reader.fname = 'crime_police.csv'
        cctv_pop = reader.csv_to_dframe()
        print(f'{cctv_pop.head()}')
        return cctv_pop

if __name__ == '__main__':
    model = Seoulcctv()
    model.hook_process()


    

    




