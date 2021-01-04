from typing import List, Dict

import pandas as pd


def write_excel(path: str, sheet_name: str, columns: List[str], data: List[Dict]):
    """将数据写入到Excel文件"""
    df = pd.DataFrame([pd.Series(item) for item in data], columns=columns)
    df.to_excel(path, sheet_name=sheet_name)
