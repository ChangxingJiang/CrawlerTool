import os


def load_string(path, encoding="UTF-8", default=None):
    """读取文件所有内容为字符串

    :param path: 文件路径
    :param encoding: 文件编码格式
    :param default: 默认返回结果
    """
    if not os.path.exists(path):
        print("读取文件失败(原因:路径不存在)")
        return default
    if not os.path.isfile(path):
        print("读取文件失败(原因:路径不是文件)")
        return default

    try:
        file = open(path, encoding=encoding)
        return file.read()
    except FileNotFoundError:
        print("读取文件失败(原因:文件未找到)")
        return default


def write_string(path, data, encoding="UTF-8", mode="w"):
    """将字符串写入到文件中

    :param path: 文件路径
    :param data: 准备写入的字符串
    :param encoding: 文件编码格式
    :param mode: 文件读取模式
    :return: <bool> 是否写入成功
    """
    try:
        with open(path, mode, encoding=encoding) as file:
            file.write(data)
            return True
    except FileNotFoundError:
        print("写入文件失败(原因:文件未找到)")
        return False
    except FileExistsError:
        print("写入文件失败(原因:文件已存在)")
        return False
