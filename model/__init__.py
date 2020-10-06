import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model.iris_model import IrisModel

from model.seoul_cctv import Seoulcctv
from model.seoul_crime import Seoulcrime

if __name__ == '__main__':
    # iris = IrisModel()
    # iris.draw_scatter()
    # iris.draw_errors()
    # iris.draw_adaline_graph()

    cctv = Seoulcctv()
    crime = Seoulcrime()
    cctv.fileinfo()
    crime.fileinfo()