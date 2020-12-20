"""
BaseSpider(object) 基础爬虫

SingleSpider(BaseSpider) 简单单线程爬虫

LoopSpider(SingleSpider) 简单单线程循环运行爬虫
"""

from .base_spider import BaseSpider
from .loop_spider import LoopSpider
from .single_spider import SingleSpider
