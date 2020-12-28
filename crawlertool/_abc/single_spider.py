from abc import ABCMeta
from abc import abstractmethod
from typing import Dict
from typing import List

from .base_spider import BaseSpider


class SingleSpider(BaseSpider, metaclass=ABCMeta):
    """简单单线程爬虫的抽象基类"""

    @abstractmethod
    def running(self, **params) -> List[Dict]:
        """执行爬虫"""
