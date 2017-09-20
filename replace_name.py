#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#import matplotlib.pyplot as plt;plt.rcdefaults()
from PIL import Image, ImageEnhance, ImageOps, ImageFile
import os
#import numpy as np
import logging

root_folder = r'D:\GK\python\test'
root_folder = unicode(root_folder , "utf8")#中文
num=0
for root,dirs,files in os.walk(root_folder):
    for file in files:
        path_img = os.path.join(root,file)
        img = Image.open(path_img)
        root_folder_new = root.replace('test','result')
        if not os.path.exists(root_folder_new):
            os.makedirs(root_folder_new)#建立多级文件夹
        file_new = root_folder_new + '\\' + str(num) + '.jpg'
        infile = root_folder_new
        outfile = file_new
        im = Image.open(path_img)
        (x, y) = im.size  # read image size
        x_s = 416
        y_s = 416
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        num = num+1
        out.save(outfile)
        print 'original size: ', x, y
        print 'adjust size: ', x_s, y_s
print "all down"