from abc import ABCMeta
from abc import abstractmethod


class BaseSpider(metaclass=ABCMeta):
    """简单单线程爬虫的抽象基类"""

    def console(self, content: str):
        print(self.__class__.__name__, ":", content)

    def log(self, content: str):
        print(self.__class__.__name__, ":", content)

    @abstractmethod
    def running(self, **params):
        """执行爬虫"""
