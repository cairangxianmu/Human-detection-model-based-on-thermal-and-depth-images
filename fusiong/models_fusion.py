import numpy as np
from ensemble_boxes_wbf import *
import pickle


def xywh2xyxy(x):
    y = np.empty_like(x)
    y[0] = x[0] - x[2] / 2.
    y[1] = x[1] - x[3] / 2.
    y[2] = x[0] + x[2] / 2.
    y[3] = x[1] + x[3] / 2.
    return y

def xyxy2xywh(x):
    y = np.empty_like(x)
    y[0] = (x[0] + x[2]) / 2.
    y[1] = (x[1] + x[3]) / 2.
    y[2] = x[2] - x[ 0]
    y[3] = x[3] - x[1]
    return y

def get_bboxesANDscores(prediction):
    bboxes = []
    scores = []
    for i in range(0,len(prediction)):
        item = prediction[i]
        bbox = item[0:4]
        bbox = xywh2xyxy(bbox)
        score = item[4]
        bboxes.append(list(bbox))
        scores.append(score)
    return bboxes, scores


def bboxesAndscores_to_prediction(bboxes, scores):
    prediction = []
    for i in range(0,len(scores)):
        bbox = bboxes[i]
        bbox = xyxy2xywh(bbox)
        score = scores[i]
        item = tuple(np.append(bbox,score))
        prediction.append(item)
    return prediction


predictions_thermal_path = 'predictions_thermal.pkl'
predictions_depth_path = 'predictions_depth.pkl'
predictions_fusion_path = 'predictions_fusion.pkl'



with open(predictions_thermal_path, 'rb') as f:
    predictions_thermal = pickle.load(f)

with open(predictions_depth_path, 'rb') as f:
    predictions_depth = pickle.load(f)



weights = [2.6, 1] 
iou_thr = 0.58 
skip_box_thr = 0.0001


predictions_fusion = {}
N=0

for key in predictions_depth:
    N=N+1
    print(N)
    prediction_thermal = predictions_thermal[key]
    prediction_depth = predictions_depth[key]

    bboxes_thermal, scores_thermal = get_bboxesANDscores(prediction_thermal)
    bboxes_depth, scores_depth = get_bboxesANDscores(prediction_depth)
    boxes_list = [bboxes_thermal,bboxes_depth]
    scores_list = [scores_thermal, scores_depth]
    labels_list = [[1 for i in range(len(scores_thermal))], [1 for i in range(len(scores_depth))]]
    boxes, scores, labels = weighted_boxes_fusion(boxes_list, scores_list, labels_list, weights=weights,
                                                  iou_thr=iou_thr, skip_box_thr=skip_box_thr)

    prediction_fusion = bboxesAndscores_to_prediction(boxes, scores)
    predictions_fusion[key] = prediction_fusion

predictionsfile = open(predictions_fusion_path, 'wb')
pickle.dump(predictions_fusion, predictionsfile, protocol=2)
