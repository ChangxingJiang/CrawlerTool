from abc import ABCMeta
from abc import abstractmethod


class SingleSpider(metaclass=ABCMeta):
    """简单单线程爬虫的抽象基类"""

    @abstractmethod
    def run(self, **params):
        """执行爬虫"""

    def console(self, content: str):
        print(self.__class__.__name__, ":", content)

    def log(self, content: str):
        print(self.__class__.__name__, ":", content)
