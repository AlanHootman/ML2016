#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image
from numpy import *

pil_im = Image.open('G:/git sources/ML2016/hw0/Lena.png')   # 写入自己本地Lena.png文件的位置
pil_im = pil_im.rotate(180)     # rotate()里面的参数是旋转度数
pil_im.save('G:/git sources/ML2016/hw0/ans2.png', 'png')    # 保存位置及名称
