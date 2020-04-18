# Receptive Field Block Net for Accurate and Fast Object Detection

By ZHC, LY, CLR, YZW

### Introduction
For more details, please refer to our https://www.sciencedirect.com/science/article/pii/S0925231219308185?via%3Dihub. 


&nbsp;
&nbsp;






### Contents
1. [Installation](#installation)
2. [Datasets](#datasets)
3. [Training](#training)
4. [Evaluation](#evaluation)
5. [Models](#models)

## Installation
- Follow RFBnet
- a huge thank to them.
  * Note: We currently only support Python 3+.
## Datasets
VOC and COCO dataset
### VOC Dataset
##### Download VOC2007 trainval & test

```Shell
# specify a directory for dataset to be downloaded into, else default is ~/data/
sh data/scripts/VOC2007.sh # <directory>
```

##### Download VOC2012 trainval

```Shell
# specify a directory for dataset to be downloaded into, else default is ~/data/
sh data/scripts/VOC2012.sh # <directory>
```
### COCO Dataset
Install the MS COCO dataset at /path/to/coco from [official website](http://mscoco.org/), default is ~/data/COCO. Following the [instructions](https://github.com/rbgirshick/py-faster-rcnn/blob/77b773655505599b94fd8f3f9928dbf1a9a776c7/data/README.md) to prepare *minival2014* and *valminusminival2014* annotations. All label files (.json) should be under the COCO/annotations/ folder. It should have this basic structure
```Shell
$COCO/
$COCO/cache/
$COCO/annotations/
$COCO/images/
$COCO/images/test2015/
$COCO/images/train2014/
$COCO/images/val2014/
```
*UPDATE*: The current COCO dataset has released new *train2017* and *val2017* sets which are just new splits of the same image sets. 

## Training
- To train MSSD(You can change datasets and models by yourself)
```Shell
python train_MSSD512VOC.py
```
## Evaluation
To evaluate a trained network:

```Shell
python test_RFB.py 

## Models

* 07+12 [MSSD512]
### Citing RFB Net


    @article{liu2017RFB,
        title = {Receptive Field Block Net for Accurate and Fast Object Detection},
        author = {Songtao Liu, Di Huang and Yunhong Wang},
        booktitle = {arxiv preprint arXiv:1711.07767},
        year = {2017}
    }

