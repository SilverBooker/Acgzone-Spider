# -*- coding:utf-8 -*-
__author__ = 'silverbooker'
__date__ = '2018/2/22 22:48'
from scrapy.cmdline import execute

import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","acgzone","-o","item.json"])