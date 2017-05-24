# -*- coding:utf-8 -*-
__author__ = 'Windows'

from scrapy import cmdline

name = "jiangsu"
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())