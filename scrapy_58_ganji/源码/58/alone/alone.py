# -*- coding:utf-8 -*-

import os
import time

#os.system("python no1.py")

#execfile('no1.py')

#爬取江苏

def go(num):
    path = 'f:\Python\jiangsu\{0}'.format(num)
    print path
    os.chdir(path)
    os.system("scrapy crawl jiangsu")
    print "Start : %s" % time.ctime()
    time.sleep( 300 )
    print "End : %s" % time.ctime()

for num in range(3,32):
    go(num)















































































