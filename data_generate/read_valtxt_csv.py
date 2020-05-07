
# coding: utf-8

import os 
import pandas as pd

path = '/media/crxm/64EDF14515570593/paper/data/iphd_valid_thermal-v2/images'
file_list = []
for i in os.listdir(path):
    file_list.append([i,30,50,60,70,'human'])
csv_file = pd.DataFrame(file_list)
csv_file.to_csv('../iphd_val_thermal.csv', index=None, header=False)
