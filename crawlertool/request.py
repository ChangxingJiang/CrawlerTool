import time

import requests


def do_request(url, method="get", **kwargs):
    """执行一次HTTP请求

    如果请求成功则返回请求结果的response对象；如果请求失败（无论任何原因）均返回None

    :param url: 请求的Url
    :param method: 请求方法
    """

    method = method.lower()
    kwargs.setdefault("timeout", 3)  # 将默认的请求时间设置为3秒

    try:
        # 依据不同的请求类型添加默认设置
        if method == "get":
            kwargs.setdefault("params", None)  # 将默认的请求参数设置为空
            kwargs.setdefault("allow_redirects", True)  # 默认设置允许重定向
        elif method == "options" or method == "head":
            kwargs.setdefault("allow_redirects", True)  # 默认设置允许重定向
        elif method == "post":
            kwargs.setdefault("data", None)  # 将默认的请求参数设置为空
            kwargs.setdefault("json", None)  # 将默认的请求参数设置为空
        elif method == "put" or method == "patch":
            kwargs.setdefault("data", None)  # 将默认的请求参数设置为空
        elif method == "delete":
            pass
        else:
            return None

        # 执行请求
        if response := requests.request(method=method, url=url, **kwargs):
            return response
        else:
            return None
    except requests.RequestException:
        return None


def try_request(url, method="get", times=3, interval=10, **kwargs):
    """尝试执行多次HTTP请求

    尝试请求times次，每次请求之间间隔interval秒；
    如果任何一次请求成功在则返回请求结果的response对象，如果每次请求都失败则返回None

    :param url: 请求的Url
    :param method: 请求方法
    :param times: 尝试请求的次数
    :param interval: 每次请求之间的间隔
    """

    for _ in range(times):
        if response := do_request(url=url, method=method, **kwargs):
            return response
        else:
            time.sleep(interval)
