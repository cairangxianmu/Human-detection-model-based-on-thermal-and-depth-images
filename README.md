## 项目名称
本文是参加IPHD竞赛的代码，内容是基于红外图像的人体检测模型，基于深度图像的人体检测模型，以及基于WBF算法在决策层融合两个模态的模型

上手指南
以下指南将帮助你在本地机器上安装和运行该项目，进行开发和测试。关于如何将该项目部署到在线环境，请参考部署小节。

安装要求
依赖环境:
	1.Python 3.5+
	2.>=PyTorch 1.1
	3.>=CUDA 9.0
	4.NCCL 2
	5.>=GCC 4.9
	6.mmcv
	7.number of GPUs >2
  8.mmdetection
我们的代码在mmdetection框架训练测试。 可以通过官网指南安装，也可以按照我写的安装教程安装环境。

测试步骤
1. 你可以下载我们的红外图像预训练模型直接进行结果测试。
2. 我们的数据是使用IPHD竞赛提供的数据，如果你想训练自己的模型，需要先将数据转化为COCO格式数据，VOC格式数据，COCO格式数据按照下面内容配置：
|mmdetection|
                    |checkpoint|
	    |                |trained_thermal.pth|
	    |                |data|
	    |                |        |instances_train.json|
	    |                |        |instances_test.json|
	    |                |        |test_images|
                       |                |        |                  |vid001.png
                       |                |        |                  |vid002.png
                       |                |        |                  |.....
	    |                |        |train_images|
                       |                |        |                  |vid001.png
                       |                |        |                  |vid002.png
                       |                |        |                  |.....
将自己的数据转化为COCO格式的代码在data_generate里。
3. 运行如下代码：

cd mmdetection
./tools/FG_dist_test.sh

运行完成后会生成predictions.pkl的结果

......一直到完成。最后阐述安装完成后的情况，展示下Demo






分解为端对端测试
解释这些测试是什么以及为什么要做这些测试
1.我是个栗子
2.我也是个栗子
3.我是栗子的哥哥



代码风格测试
解释这些测试是什么以及为什么要做这些测试
1.我是个栗子
2.我也是个栗子
3.我是栗子的哥哥



部署
对以上的安装步骤进行补充说明，描述如何在在线环境中安装该项目。



使用到的框架
Dropwizard - Web框架
Maven - 依赖属性管理
ROME - 生成RSS源



贡献者
请阅读CONTRIBUTING.md 查阅为该项目做出贡献的开发者。


版本控制
该项目使用SemVer进行版本管理。您可以在repository参看当前可用版本。



作者
地球上的盐味
您也可以在贡献者名单中参看所有参与该项目的开发者。



版权说明
该项目签署了MIT 授权许可，详情请参阅 LICENSE.md



鸣谢
该项目参考了XXX的 XXX
灵感来源于XXX
感谢女友的支持和陪伴
