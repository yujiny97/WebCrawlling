import pandas as pd
import numpy as np
import os
excel_file='값.xlsx'
base_dir_for_ex='C:\\Users\\i5533\\OneDrive\\바탕 화면\\바탕화면정리\\빅데이터공모전\\딥러닝\\데이터엑셀'
excel_dir=os.path.join(base_dir_for_ex,excel_file)

df_from_excel = pd.read_excel(excel_dir,
                              sheet_name = 'Sheet1',
                              header=2,
                              names=['origin','함수1','함수2','버섯이름','현재_존재값','최소','적절'],
                              dtype={'origin': str,
                                     '함수1': str,
                                     '함수2': str,
                                     '버섯이름': str,
                                     '현재_존재값': int,
                                     '최소': int,
                                     '적절': int
                                }
                              )
df_from_excel['적절']