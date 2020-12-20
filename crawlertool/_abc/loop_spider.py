import threading
import time
from abc import ABCMeta
from abc import abstractmethod
from typing import SupportsFloat

from .single_spider import SingleSpider


class LoopSpider(SingleSpider, threading.Thread, metaclass=ABCMeta):
    def __init__(self, interval: SupportsFloat = 1):
        super().__init__()
        self.interval = interval

        # 暂停标记
        self._pause = threading.Event()
        self._pause.set()  # 将暂停标记设置为True(表示没有暂停)

        # 结束标记
        self._stop = threading.Event()
        self._stop.set()  # 将结束标记设置为True(表示没有结束)

        # 爬虫运行计数器(从0开始)
        self.num = 0

    def run(self):
        while self._stop.isSet():  # 当结束标记为True时则继续循环(表示还没有结束)
            self._pause.wait()  # 等待暂停标记为True(当暂停标记变为True时则直接返回,为False时则阻塞直到为True后返回)

            self.running()  # 执行爬虫
            time.sleep(float(self.interval))  # 执行延时

            self.num += 1  # 运行计时器叠加

    @abstractmethod
    def write(self, **params):
        """每次循环执行爬虫的结果处理(在self.running()中调用)"""

    def pause(self):
        self._pause.clear()  # 将暂停标记设置为False(表示正在暂停)

    def resume(self):
        self._pause.set()  # 将暂停标记设置为True(表示没有暂停)

    def stop(self):
        self._pause.set()  # 将暂停标记设置为True(表示没有暂停):用以使当前被暂停的一次可以被执行
        self._stop.clear()  # 将结束标记设置为False(表示已经结束)
