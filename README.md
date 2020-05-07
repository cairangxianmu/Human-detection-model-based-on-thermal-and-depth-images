# 融合红外和深度图像的人体检测模型
本文是参加[IPHD竞赛](http://chalearnlap.cvc.uab.es/challenge/34/description/)的代码，内容是基于红外图像的人体检测模型，基于深度图像的人体检测模型，以及基于[WBF算法](https://www.groundai.com/project/weighted-boxes-fusion-ensembling-boxes-for-object-detection-models/1)在决策层融合两个模态的模型
![单模型与融合模型](/fusion.png "单模型与融合模型结果对比")

# 上手指南
以下指南将帮助你在本地机器上安装和运行该项目，进行开发和测试。关于如何将该项目部署到在线环境，请参考部署小节。

# 安装要求
依赖环境:
1. Python 3.5+
2. >=PyTorch 1.1
3. >=CUDA 9.0
4. NCCL 2
5. >=GCC 4.9
6. mmcv
7. number of GPUs >2
8. mmdetection
我们的代码在mmdetection框架训练测试。 可以通过[官网指南](https://github.com/open-mmlab/mmdetection/blob/master/docs/install.md)安装，也可以按照我写的[安装教程](https://blog.csdn.net/qq_33897832/article/details/103995636)安装环境。
# 红外图像增强
我们对红外图像进行了增强去去燥，代码在文件下，效果如下：
![图像增强](/图像.png "图像增强方法效果")
# 测试步骤
1. 你可以下载我们的[红外图像预训练模型](https://pan.baidu.com/s/1iQj0BdytnkcUHHL2B25wcA),提取码：asgg 直接进行结果测试。
2. 我们的数据是使用IPHD竞赛提供的数据:[下载地址](http://chalearnlap.cvc.uab.es/dataset/34/description/)，如果你想训练自己的模型，需要先将数据转化为COCO格式数据，VOC格式数据，COCO格式数据按照下面内容配置：

```
mmdetection
├── checkpoint
|   ├── trained_thermal.pth
├── data
|   ├── coco
|   |   ├──annotations
|   |   |   ├── instances_train.json
|   |   |   ├── instances_test.json
|   |   ├── train_images
|   |   |   ├── vid001.png
|   |   |   ├── vid002.png
|   |   |   ├── ...
|   |   ├── test_images
|   |   |   ├── vid001.png
|   |   |   ├── vid002.png
|   |   |   ├── ...
```

将自己的数据转化为COCO格式的代码在[data_generate](https://github.com/cairangxianmu/Human-detection-model-based-on-thermal-and-depth-images/tree/master/data_generate)里

3. 运行如下代码：

```
cd mmdetection 
./tools/FG_dist_test.sh
```

运行完成后会生成predictions.pkl的结果
如果需要在图片上显示测试结果，运行如下代码（需要opencv环境支持）：

```
#python tools/test.py ${配置文件} ${训练好的模型} [--out ${保存输出结果的位置}] [--eval ${验证类型}] [--show](此项可显示每个图像检测后的结果)
python tools/test.py configs/faster_rcnn_r50_fpn_1x.py work_dirs/faster_rcnn_r50_fpn_1x/epoch1.pth --eval bbox --show
```

更多模型训练及测试操作，参考我的[博文](https://blog.csdn.net/qq_33897832/article/details/103995636)，及[mmdetection官网](https://github.com/open-mmlab/mmdetection/blob/master/docs/getting_started.md)


# 使用到的框架
我们使用的框架为商汤科技和香港中文大学开源的一个基于Pytorch实现的深度学习目标检测工具箱[mmdetection](https://github.com/open-mmlab/mmdetection)，支持Faster-RCNN，Mask-RCNN，Fast-RCNN，Cascade-RCNN等主流目标检测框架。可以快速部署自己的模型。


# 作者
四川大学BRL实验室
