
# coding: utf-8

# In[23]:


import os
import pandas as pd
from sklearn.model_selection import train_test_split

def ReadTxt(txt_path,rootdir):
    W = 213
    H = 120
    label = []
    Y = []
    image = []
    labelfile = open(txt_path,'r')
    while True: 
        imagename = labelfile.readline()
        if not imagename:
            break
        image.append(imagename)
        
    for files in image:
        file = os.path.join(rootdir, files.split(".")[0] + ".txt") 
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
                print("file", filename)
                label.append([filename, x, y, x + w, y + h, 'human'])
                Y.append(class_id)
    return label, Y

txt_path = "E:/paper/data/all_good_thermal_im.txt"
label_path = "E:/paper/data/iphd_train_thermal-v2/labels"
labels,Y =  ReadTxt(txt_path,label_path)
csv_labels = open("./iphd_good_train_thermal.csv","w")
for filename,bbox1, bbox2, bbox3, bbox4, label in labels:
    print(filename,bbox1, bbox2, bbox3, bbox4, label)
    csv_labels.write(filename+","+str(bbox1)+","+str(bbox2)+","+str(bbox3)+","+str(bbox4)+","+"human"+"\n")
csv_labels.close()
print("Successfully write to file")
