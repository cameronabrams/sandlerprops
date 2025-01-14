# Author: Cameron F. Abrams <cfa22@drexel.edu>

import pandas as pd
import os
from . import resources

datafile_path=os.path.join(os.path.split(resources.__file__)[0],'data','properties_database.csv')

class Properties:
    def __init__(self):
        self.D=pd.read_csv(datafile_path,header=0,index_col=0)
        