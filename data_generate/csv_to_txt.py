import os
import pandas as pd
import time
from tqdm import tqdm, trange

def WriteTxt(rootdir, df_csv):
    print("length", len(df_csv))
    for i in trange(len(df_csv)):
        time.sleep(0.1)
        files = df_csv['filename'][i].split(".")[0] + ".txt"
        file = os.path.join(rootdir, files) 
        with open(file, 'a+') as write_file:
                _, W, H, _, xmin, ymin, xmax, ymax  = df_csv.loc[i]
                w = (xmax - xmin) / W
                h = (ymax - ymin)/ H
                x = (xmax - (xmax-xmin)/2) / W
                y = (ymax - (ymax-ymin)/2) / H
                #tqdm.description("file",files)
                #print("write_to",files)
                write_file.write(" ".join(['1',str(x), str(y), str(w), str(h), "\n"]))


df_csv = pd.read_csv('../images_val_depth_v2.csv')

txt_path = "/media/crxm/64EDF14515570593/paper/data/images_val_depth/labels_txt_v2"
WriteTxt(txt_path,df_csv)
print("Successfully write to file")
