# config.py
import os.path

# gets home dir cross platform
home = os.path.expanduser("~")
ddir = os.path.join(home,"data/VOCdevkit/")

# note: if you used our download scripts, this should be right
VOCroot = ddir # path to VOCdevkit root dir
COCOroot = os.path.join(home,"data/coco/")


#RFB CONFIGS


VOC_300 = {
    'feature_maps' : [38, 19, 10, 5, 3, 1],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100, 300],

    'min_sizes' : [30, 60, 111, 162, 213, 264],

    'max_sizes' : [60, 111, 162, 213, 264, 315],

    'aspect_ratios' : [[2], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}

VOC_300_1 = {
    'feature_maps' : [38, 19, 10, 5, 3, 1],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100, 300],

    'min_sizes' : [30, 60, 111, 162, 213, 264],

    'max_sizes' : [60, 111, 162, 213, 264, 315],

    'aspect_ratios' : [[2], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
VOC_300_2 = {
    'feature_maps' : [38, 19, 10, 5, 3],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100],

    'min_sizes' : [30, 60, 111, 162, 213],

    'max_sizes' : [60, 111, 162, 213, 315],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
VOC_300_3 = {
    'feature_maps' : [38, 19, 10, 5, 3],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100],

    'min_sizes' : [30, 60, 111, 162, 213],

    'max_sizes' : [60, 111, 162, 213, 315],

    'aspect_ratios' : [[2], [2, 3], [2, 3], [2, 3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
VOC_320 = {
    'feature_maps' : [40, 20, 10, 5, 3],

    'min_dim' : 320,

    'steps' : [8, 16, 32, 64, 100],

    'min_sizes' : [30, 60, 111, 162, 213],

    'max_sizes' : [60, 111, 162, 213, 315],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}

VOC_512= {
    'feature_maps' : [64, 32, 16, 8, 4, 2, 1],

    'min_dim' : 512,

    'steps' : [8, 16, 32, 64, 128, 256, 512],

    'min_sizes'  : [35.84, 76.8, 153.6, 230.4, 307.2, 384.0, 460.8 ],

    'max_sizes'  : [76.8, 153.6, 230.4, 307.2, 384.0, 460.8, 537.6],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3], [2], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
VOC_512_2={
    'feature_maps' : [64, 32, 16, 8, 4, 2],

    'min_dim' : 512,

    'steps' : [8, 16, 32, 64, 128, 256],

    'min_sizes'  : [35.84, 76.8, 153.6, 230.4, 307.2, 384.0 ],

    'max_sizes'  : [76.8, 153.6, 230.4, 307.2, 384.0,  537.6],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
VOC_512_3={
    'feature_maps' : [64, 32, 16, 8, 4],

    'min_dim' : 512,

    'steps' : [8, 16, 32, 64, 128],

    'min_sizes'  : [35.84, 76.8, 153.6, 230.4, 307.2],

    'max_sizes'  : [76.8, 153.6, 230.4, 307.2,  537.6],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
COCO_300 = {
    'feature_maps' : [38, 19, 10, 5, 3, 1],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100, 300],

    'min_sizes' : [21, 45, 99, 153, 207, 261],

    'max_sizes' : [45, 99, 153, 207, 261, 315],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
COCO_300_1 = {
    'feature_maps' : [38, 19, 10, 5, 3],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100],

    'min_sizes' : [21, 45, 99, 153, 207],

    'max_sizes' : [45, 99, 153, 207, 315],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
COCO_300_11 = {
    'feature_maps' : [38, 19, 10, 5, 3],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100],

    'min_sizes' : [11, 35, 89, 143, 197],

    'max_sizes' : [35, 89, 143, 197, 305],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
COCO_512_2= {
    'feature_maps' : [64, 32, 16, 8, 4, 2],

    'min_dim' : 512,

    'steps' : [8, 16, 32, 64, 128, 256],

    'min_sizes' : [20.48, 51.2, 133.12, 215.04, 296.96, 378.88],

    'max_sizes' : [51.2, 133.12, 215.04, 296.96, 378.88, 542.72],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
COCO_512_3= {
    'feature_maps' : [64, 32, 16, 8, 4, 2],

    'min_dim' : 512,

    'steps' : [8, 16, 32, 64, 128, 256],

    'min_sizes' : [20.48, 51.2, 133.12, 215.04, 296.96, 378.88],

    'max_sizes' : [51.2, 133.12, 215.04, 296.96, 378.88, 542.72],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3], [2,3]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}
COCO_512= {
    'feature_maps' : [64, 32, 16, 8, 4, 2, 1],

    'min_dim' : 512,

    'steps' : [8, 16, 32, 64, 128, 256, 512],

    'min_sizes' : [20.48, 51.2, 133.12, 215.04, 296.96, 378.88, 460.8],

    'max_sizes' : [51.2, 133.12, 215.04, 296.96, 378.88, 460.8, 542.72],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2,3], [2], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}

COCO_mobile_300 = {
    'feature_maps' : [19, 10, 5, 3, 2, 1],

    'min_dim' : 300,

    'steps' : [16, 32, 64, 100, 150, 300],

    'min_sizes' : [45, 90, 135, 180, 225, 270],

    'max_sizes' : [90, 135, 180, 225, 270, 315],

    'aspect_ratios' : [[2,3], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}