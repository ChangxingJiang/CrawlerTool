import time

import requests


def do_request(url, method="get", **kwargs):
    """执行HTTP请求：如果请求成功则返回请求结果；如果请求失败则返回None"""

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
    """尝试执行HTTP请求：尝试请求times次，每次请求之间间隔interval秒，如果最终请求失败则返回None"""

    for _ in range(times):
        if response := do_request(url=url, method=method, **kwargs):
            return response
        else:
            time.sleep(interval)
