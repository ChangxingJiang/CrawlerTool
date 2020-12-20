from abc import ABCMeta
from abc import abstractmethod

from .base_spider import BaseSpider


class SingleSpider(BaseSpider, metaclass=ABCMeta):
    """简单单线程爬虫的抽象基类"""

    @abstractmethod
    def running(self, **params):
        """执行爬虫"""

