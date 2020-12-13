from abc import ABCMeta


class BaseSpider(metaclass=ABCMeta):
    """简单单线程爬虫的抽象基类"""

    def console(self, content: str):
        print(self.__class__.__name__, ":", content)

    def log(self, content: str):
        print(self.__class__.__name__, ":", content)
