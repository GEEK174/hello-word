# -*- coding: utf-8 -*-
# coding=gbk

import string
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

if __name__ == '__main__':
    num_txt = r'D:\GK\python\errorAll_6_noflip.txt'
    # num_txt = unicode(num_txt, "utf8")
    i = 0
    step_list = []
    class_0_ra = []

    class_0_pa = []
    f1 = open(num_txt, 'r')
    linesList = f1.readlines()
    for line in linesList:
        i = i + 1
        tmp = line.strip('\n').split(':')
        # if (i%16==1 and '00'in line):
        if ('model' in line):
            x = tmp[1]
            step_list.append(x)
            print step_list
        elif ("allerror" in line):
            y = tmp[1]
            class_0_ra.append(y)
            print class_0_ra
        f1.close()

    plot1 = pl.plot(step_list, class_0_ra,'r')  # ,label=$cos( x^2)$)

    # plot6=pl.plot(step_list,  class_0_pa,'y')
    # plot7=pl.plot(step_list,  class_1_pa,'#000000')
    # plot8=pl.plot(step_list,  class_2_pa,'c')
    # plot9=pl.plot(step_list,  class_3_pa,'#800080')
    # plot10=pl.plot(step_list,  class_4_pa,'#87CEEB')

    #pl.x('threshold')
    #pl.y('accuracy')
    pl.ylim(3, 5)
    pl.xlim(5000, 10000)
    pl.title('threshold/accuracy')
    # pl.legend([plot1, plot2], ('red line', 'green circles'), "best", numpoints=1)
    pl.show()

