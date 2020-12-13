import json
from json import JSONDecodeError
from typing import Dict

from .file import load_string
from .file import write_string


def load_json(path, encoding="UTF-8", default=None) -> Dict:
    """读取文件所有内容为Json格式对象

    :param path: 文件路径
    :param encoding: 文件编码格式
    :param default: 默认返回结果
    """
    try:
        if string := load_string(path, encoding):
            return json.loads(string)
    except JSONDecodeError:
        print("读取Json文件失败(原因:目标文件不是Json文件)")
        return default


def write_json(path, data, encoding="UTF-8", ensure_ascii=False):
    """将Json格式数据写入到文件中

    :param path: 文件路径
    :param data: 准备写入的Json对象
    :param encoding: 文件编码格式
    :param ensure_ascii: 是否要求所有字符均为ASCII编码字符（即是否将中文替换为ASCII编码）
    :return: <bool> 是否写入成功
    """
    write_string(path, json.dumps(data, ensure_ascii=ensure_ascii), encoding=encoding)
