# -*- coding:utf-8 -*-

import os
import time

#os.system("python no1.py")

#execfile('no1.py')

#赶集网爬取江苏

def go(num):
    path = 'f:\Python\ganji_jiangsu\{0}'.format(num)
    print path
    os.chdir(path)
    os.system("scrapy crawl ganji")
    print "__{0}__Start : %s".format(num) % time.ctime()
    time.sleep( 300 )
    print "__{0}__End : %s".format(num) % time.ctime()

for num in range(1,13):
    go(num)