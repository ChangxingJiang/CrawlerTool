import re


def extract_number_from_string(string: str):
    """字符串中数字的提取器（中文模式：支持“万”、“万亿”、“亿”等数值单位）

    提取字符串中的第一个数字，支持小数点、E、正负号、逗号间隔、中文数值单位的识别、计算

    :param string 需要提取数字的字符串
    :return 提取的数字，如果是整数则返回int格式数字，如果不是整数则返回float格式数字
    """
    if pattern := re.search(r"[-+]?([\d,]+\.?\d*|\.\d+)(e[-+]?\d+|)万?亿?", string):
        string = pattern.group().replace(",", "")
        string, p1 = re.subn(r"万", "", string)
        string, p2 = re.subn(r"亿", "", string)
        result = float(string) * pow(10, p1 * 4 + p2 * 8)
        return int(result) if int(result) == result else result
    else:
        return None
