import json
import pandas as pd
import collections
import pickle

W, H = 213, 120
txt_path = 'filename_test.txt'
json_path = 'faster_rcnn_x101_64x4d_fpn_1x_thermal_painting_test_e1.pkl.bbox.json'

filename = pd.read_table(txt_path, header=None, sep='\t')
filename = filename.values.flatten().tolist()

with open(json_path, 'r') as f:
    data = json.load(f)   
    box = [[] for i in range(len(filename))]
    print(len(data))
    for i in range(len(data)):
        image_id = data[i]['image_id']
        xmin,ymin,w,h = data[i]['bbox']
        score = data[i]['score']
        if score < 0.5:
            continue
        x = (xmin + w / 2) / W
        y = (ymin+ h / 2) / H
        w = w / W
        h = h / H
        box[image_id].append((x,y,w,h,score))

print(len(filename),len(box))
d = {}
for i, key in enumerate(filename):
    d.setdefault(key,box[i])
dic = collections.OrderedDict(d)
file = open(r"predictions.pkl",'wb')
pickle.dump(dic,file,protocol=2)
print("Successful write file predictions.pkl")
