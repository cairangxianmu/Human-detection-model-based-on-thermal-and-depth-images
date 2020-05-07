
# coding: utf-8

# In[23]:


import os
import pandas as pd
from sklearn.model_selection import train_test_split

def ReadTxt(rootdir):
    W = 213
    H = 120
    label = []
    for files in os.listdir(rootdir):
        file = os.path.join(rootdir, files) 
        with open(file, 'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                class_id, x, y, w, h = map(eval,line.split())
                filename = files.split(".")[0] + ".png"
                w = w * W
                h = h * H
                x = (x * W) - (w / 2)
                y = (y * H) - (h / 2)
                label.append([filename, x, y, x + w, y + h, 1])
    return label

txt_path = "/media/crxm/64EDF14515570593/paper/data/iphd_train_thermal-v2/labels_filtered"
labels =  ReadTxt(txt_path)
csv_labels = open("../iphd_train_thermal_filter.csv","w")
for filename,bbox1, bbox2, bbox3, bbox4, label in labels:
    print(filename,bbox1, bbox2, bbox3, bbox4, label)
    csv_labels.write(filename+","+str(bbox1)+","+str(bbox2)+","+str(bbox3)+","+str(bbox4)+","+"human"+"\n")
csv_labels.close()
print("Successfully write to file",len(labels))
