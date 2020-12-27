import time

import requests


def do_request(url, params=None, **kwargs):
    """执行HTTP请求：如果请求成功则返回请求结果；如果请求失败则返回None"""

    # 将默认的请求时间设置为3秒
    if "timeout" not in kwargs:
        kwargs["timeout"] = 3

    try:
        if response := requests.get(url=url, params=params, **kwargs):
            return response
    except requests.RequestException:
        return None


def try_request(url, params=None, times=3, interval=10, **kwargs):
    """尝试执行HTTP请求：尝试请求times次，每次请求之间间隔interval秒，如果最终请求失败则返回None"""
    for _ in range(times):
        if response := do_request(url=url, params=params, **kwargs):
            return response
        else:
            time.sleep(interval)
