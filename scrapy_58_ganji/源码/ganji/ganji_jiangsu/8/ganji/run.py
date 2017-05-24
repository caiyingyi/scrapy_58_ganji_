# -*- coding:utf-8 -*-
__author__ = 'Windows'

from scrapy import cmdline

name = "ganji"
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())

