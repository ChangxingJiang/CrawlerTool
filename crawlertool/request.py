import time

import requests


def do_request(url, headers=None, proxies=None, timeout=3):
    """执行HTTP请求：如果请求成功则返回请求结果；如果请求失败则返回None"""
    try:
        if response := requests.get(url=url, headers=headers, proxies=proxies, timeout=timeout):
            return response.content.decode(encoding="UTF-8", errors="ignore")
    except requests.RequestException:
        return None


def try_request(url, headers=None, proxies=None, times=3, interval=10, timeout=3):
    """尝试执行HTTP请求：尝试请求times次，每次请求之间间隔interval秒，如果最终请求失败则返回None"""
    for _ in range(times):
        if response := do_request(url=url, headers=headers, proxies=proxies, timeout=timeout):
            return response
        else:
            time.sleep(interval)
