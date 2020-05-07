import cv2
import numpy as np
import os
from io import StringIO
from pathlib import Path
from PIL import Image, ImageOps
from skimage import exposure
import pickle
from collections import Counter
import copy
from sklearn import mixture

thermalpath = '/media/crxm/64EDF14515570593/paper/data/iphd_test_thermal/images/'
imagelist = os.listdir(thermalpath)

predictions=pickle.loads(open(r'predictions_faster_rcnn_x1010_thermal_painting426x240_changeRGB_0.7178.pkl','rb').read())

for i in range(100 ,len(imagelist)) :
    # for i in range(len(imagelist)):
    print(i)
    vid_name = imagelist[i][0:8]
    vidnum = vid_name[3:]

    im = cv2.imread(thermalpath+imagelist[i], cv2.IMREAD_UNCHANGED)
    #im= exposure.equalize_adapthist(im, kernel_size=16, nbins=256)
    if np.any(im==None):
        print('im==None')
        continue
    im_vec=im.ravel()
    hist_im=Counter(im_vec)
    im_v=np.sort([hist_im.keys()])
    im_vec=im_vec.reshape((len(im_vec),1))
    g=mixture.GaussianMixture(n_components=2,covariance_type='spherical',tol=0.1,max_iter=1000)
    ret=g.fit(im_vec)
    mid=np.mean(ret.means_)
    signal=im_vec[im_vec>mid]
    mu=np.mean(signal)
    sigma=np.sqrt(np.var(signal))
    low=mu-0.7*sigma
    high=mu+0.7*sigma
    im[im<low]=round(low)
    im[im>high]=round(high)
    im=(255*((im-low)/(high-low))).astype(np.uint8)
    im_color=cv2.applyColorMap(im,cv2.COLORMAP_HOT)
    mask = copy.copy(im_color)
    mask[mask!=0] = 1
    mask = 1 - mask
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    im = cv2.inpaint(im_color, mask, 3, 1)
    roi=predictions[imagelist[i][:-4]]
    [h,w]=im.shape[0:2]
    for j in range(0,len(roi)):
        bbox = roi[j]
        if bbox[4]<0.5:
             continue
        bbox = np.array(bbox) * np.array([w, h, w, h ,1])
        cv2.rectangle(im, (np.int(bbox[0] - bbox[2] / 2), np.int(bbox[1] - bbox[3] / 2)),
                      (np.int(bbox[0] + bbox[2] / 2), np.int(bbox[1] + bbox[3] / 2)), (0, 255, 0), 3)
        if j%50==0:
            cv2.destroyAllWindows()

    #cv2.imshow(imagelist[i],im)
    cv2.imwrite(imagelist[i],im, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(i)
