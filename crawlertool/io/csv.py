from typing import List, Dict

import pandas as pd


def write_csv(path: str, columns: List[str], data: List[Dict]):
    """将数据写入到csv文件"""
    df = pd.DataFrame([pd.Series(item) for item in data], columns=columns)
    df.to_csv(path, mode="a+",  # 追加模式
              header=False,  # 不添加列名行
              index=False)  # 不添加索引列
