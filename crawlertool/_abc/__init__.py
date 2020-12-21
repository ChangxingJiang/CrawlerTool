"""
对于单次运行的爬虫，通过调用running()方法执行爬虫，爬虫运行结果为running()方法的返回值；
对于循环运行的爬虫，通过调用start()方法执行爬虫，爬虫运行结果通过参数传递给write()方法，通过重写write()方法处理返回值。

爬虫抽象基类列表：
BaseSpider(object) 基础爬虫
SingleSpider(BaseSpider) 简单单线程爬虫
LoopSpider(SingleSpider) 简单单线程循环运行爬虫
"""

from .base_spider import BaseSpider
from .loop_spider import LoopSpider
from .single_spider import SingleSpider
