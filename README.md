# tibetan-character-recognition

## Data
TPCD Datasets数据集进行图像分类。它是《Research on multi font Tibetan printed character recognition based on Neural Network》文章的藏文字丁图片数据集-其中训练集为39168、测试集为3917、验证集为5875个。TPCD数据集拥有544个藏文字丁由48960张黑白图片构成并且这些黑白的PNG图像以5184像素组成，每张图片的大小为72*72，由544类藏文字丁构成。

## Models
实验部分由前馈神经网络 FNN 、支持向量机SVM，参数较少的CNN-small和 CNN四部分组成。


### Requirements
Python 3.6
Tensorflow 2.2.0
keras 2.3.1
opencv-contrib-python 4.3.0.36

### Dependencies
os
re
PIL
cv2
numpy
pandas 
matplotlib
tensorflow
sklearn
scikitplot
joblib
tensorboard

### Experiment
本实验随着字体数目的减少识别率、召回率和F1值增大，即：字体数量与识别率、召回率和F1值成反比关系。由 /tibetan-character-recognition/data文件夹中的10个字体种类、30个字体种类、50个字体种类、80个字体种类、90个字体种类可验证。文件夹TPCD-bzhb、
TPCD-hzbb和Original-Img包括所有构建的藏文印刷体字丁数据集（48960张图像），其中文件夹TPCD-bzhb是白字黑背景的数据、TPCD-hzbb是黑字白背景数据和原始Original-Img数据，本文在TPCD-bzhb数据集的实验结果更好。
